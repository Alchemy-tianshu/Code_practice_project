import requests
import time
import re
import json

count = 0

headers = {
'Cookie': 'uuid_n_v=v1; uuid=AF3D1220948011E8B2AA9FA8B2681702285785F0A8C6440893B814F988D9E847; _csrf=7e74e8ba9e19ad80506d12f9c59ca4d0663c09568af4bd8ab119e7fa42cf0406; _lxsdk_cuid=164eec2d003c8-08f976660a5271-2711f38-144000-164eec2d003c8; _lxsdk=AF3D1220948011E8B2AA9FA8B2681702285785F0A8C6440893B814F988D9E847; __mta=210171562.1533014102076.1533015465347.1533015624851.12; _lxsdk_s=164eec2d004-581-309-f99%7C%7C29',
'Host': 'maoyan.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36',
}

# 获取首页
def get_page(url):
    time.sleep(2)
    response = requests.get(url,headers=headers)
    if response.status_code == requests.codes.ok:
        return response.text
    return None

# 解析第一页
def parse_page(html):
    pattern = re.compile('<i.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        global count
        count = count + 1
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip()+item[6].strip()
        }

# 存储数据
def save_to_json(content):
    with open('data.txt','a',encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False,))

# 主程序
def main(offset):
    url = "http://maoyan.com/board/4?"+str(offset)
    html = get_page(url)
    for item in parse_page(html):
        save_to_json(item)

if __name__ == "__main__":
    for i in range(10):
        offset = i*10
        main(offset)
        time.sleep(1)
    print(count+"条数据")