# import requests
#
# response = requests.get("https://www.baidu.com/")
#
# # Response类型
# print(type(response))
# # 状态码
# print(response.status_code)
# # 文本类型
# print(type(response.text))
# # 文本内容
# print(response.text)
# # cookies
# print(response.cookies)

# import requests
#
# # 一般情况下不这样书写，都是伪造一个字典
# # response =  requests.get('http://httpbin.org/get?name=angle&like=dongman')
#
# params = {
#     'name':'angle',
#     'like':'dongmnae',
# }
# response = requests.get("http://httpbin.org/get", params=params)
# print(type(response.text))
# print(response.text)
# print(type(response.json()))

'''
<a class="question_link" href="/question/270883846/answer/453687656" target="_blank" data-id="22471511" data-za-element-name="Title">
哪本书是你只要有机会就会强烈推荐的？为什么？
</a>
'''
# import requests,re
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
#
# response = requests.get('https://www.zhihu.com/explore',headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern,response.text)
# print(titles)

# import requests
# response = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico','wb') as f:
#     f.write(response.content)


# import requests
#
# data = {'name': 'germey', 'age': '22'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)

# import requests
#
# r = requests.get('http://www.jianshu.com')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)

import requests

r = requests.get('http://www.jianshu.com')

exit() if not r.status_code == requests.codes.ok else print("请求成功")