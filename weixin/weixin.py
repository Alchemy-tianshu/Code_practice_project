import config,requests,re,json,logging,html,time
from random import random
from models import Article
from mongoengine import connect
from datetime import datetime
from urllib.parse import urlparse

base_url = "https://mp.weixin.qq.com"
search_url = "https://mp.weixin.qq.com/cgi-bin/searchbiz?"
appmsp_url = "https://mp.weixin.qq.com/cgi-bin/appmsg?"
profile_url = "https://mp.weixin.qq.com/mp/profile_ext"
message_url = "https://mp.weixin.qq.com/mp/getappmsgext"

class wechatSpider():

    def __init__(self):
        self.headers = self.headers_to_dict(config.INIT_HEADERS)
        # print(self.headers)

    def crawl_message(self,offset=0):
        '''
        爬去公众号文章，每次10条数据
        :param offset:
        :return:
        '''
        params = '''action=getmsg&__biz=MzA3NTE5MzQzMA==&f=json&offset={}&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=LGth1xNeWdpgxHksnTPY1F0tcPlqtRyO%2FSiMSeadzPI%3D&wxtoken=&appmsg_token=968_BTl67wXPJHLBjbJU4Lp3Q_mCR1JZ5XdfKSHlvw~~&x5=1&f=json'''.format(offset)

        params = wechatSpider.str_to_dict(params)
        response = requests.get(profile_url,params=params,headers=self.headers,verify=False)
        result = response.json()
        print(result)
        general_msg_list = result["general_msg_list"]
        wechatSpider.save_to_mongo(general_msg_list)
        self.parse(result)

    def parse(self,result):
        '''
        解析json数据，根据can_msg_continue字段的结果判断是不是要继续爬取
        :param self:
        :param result:
        :return:
        '''
        logging.info(json.dumps(result,ensure_ascii=False))
        if result["ret"] == 0 and result["can_msg_continue"] == 1:
            logging.info(result["next_offset"])
            print(result['next_offset'])
            time.sleep(3)
            self.crawl_message(result["next_offset"])

    @staticmethod
    def save_to_mongo(msg):
        msg = msg.replace('\/','/')
        msg = json.loads(msg)
        msg_list = msg["list"]
        for msg in msg_list:
            push_time = msg.get("comm_msg_info").get("datetime")
            print(push_time)
            # 非图文消息没有此字段
            message_info = msg.get("app_msg_ext_info")
            if message_info:
                wechatSpider._insert(message_info,push_time)
                # 多图文推送，主文章下的文章推送
                multi_msg_info = message_info.get("multi_app_msg_item_list")
                for msg_info in multi_msg_info:
                    wechatSpider._insert(msg_info,push_time)
            else:
                logging.warning("此消息不是图文推送,data={}".format(json.dumps(msg.get("comm_msg_info"))))

    @staticmethod
    def _insert(items,push_time):
        keys = 'title,author,content_url,digest,cover,source_url'.split(',')
        sub_data = wechatSpider.sub_dict(items,keys)
        article = Article(**sub_data)
        push_time = datetime.fromtimestamp(push_time)
        article.push_time = push_time
        logging.info("save data {}".format(article.title))
        try:
            article.save()
            time.sleep(2)
            wechatSpider.message(article)
        except Exception as e:
            logging.error("保存失败 data={}".format(article.to_json()),exc_info=True)

    @staticmethod
    def message(article):
        '''
        爬取文章评论数和阅读数
        :param article:
        :return:
        '''
        data_url_params = '''
        '''
        # 获取文章请求链接的参数
        data_url_params = wechatSpider.str_to_dict(config.DATA_URL_PARAMS)

        # 将文章的链接url转义处理
        content_url = html.unescape(article.content_url)
        # 文章标题链接里面的参数
        content_url_params = urlparse(content_url).query
        content_url_params = wechatSpider.str_to_dict(content_url_params)

        data = wechatSpider.str_to_dict(config.BODY)
        # 用文章链接里面的参数更新body里面的参数，因为body里面的一些参数的值和文章链接里面参数一样
        data.update(content_url_params)

        headers = wechatSpider.headers_to_dict(config.MESSAGE_HEADERS)
        response = requests.post(message_url,data=data,verify=False,params=data_url_params,headers=headers)
        result = response.json()
        if result.get('appmsgstat'):
            appmsgstat = result.get('appmsgstat')
            article.read_num = appmsgstat.get("read_num")
            article.like_num = appmsgstat.get('like_num')
            logging.info("阅读数:{},点赞数:{}".format(article.read_num,article.like_num))
            try:
                article.reward_num = result.get('reward_total_count')
            except:
                logging.info("该篇文章没有开启赞赏功能")
            article.update_date = datetime.now()
            article.save()
        else:
            logging.warning(u"没有获取的真实数据，请检查请求参数是否正确，返回的数据为：data=%s" % response.text)

    @staticmethod
    def str_to_dict(str=""):
        '''
        将字符串形式的params变成字典格式
        :param str:
        :return: o_params
        '''
        params = str.replace(' ','').replace('\n','').replace('\t','')
        params = params.split('&')
        o_params = {}
        for param in params:
            param = param.split('=',1)
            o_params.update({param[0]:param[1]})
        return o_params

    @staticmethod
    def headers_to_dict(headers):
        '''
        将headers字符串变成字典
        :param headers:
        :return:
        '''
        # 去掉空白字符
        headers = headers.replace(' ', '').replace('\t', '')
        headers = headers.split('\n')
        o_headers = {}
        for header in headers[1:-1]:
            s_header = header.split(':', 1)
            o_headers.update({s_header[0]:s_header[1]})
        return o_headers

    @staticmethod
    def sub_dict(items,keys):
        return {key:html.unescape(items[key]) for key in items if key in keys}

if __name__ == "__main__":
    connect("共青团中央",host="localhost",port=27017)
    wechatSpider().crawl_message()