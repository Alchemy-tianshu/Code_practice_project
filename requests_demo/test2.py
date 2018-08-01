# import requests
#
# files = {'file':open('favicon.ico','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)


# import requests
#
# response = requests.get('https://www.baidu.com')
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key+"="+value)
#
# import requests
#
# headers = {
#     'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# # print(r.cookies)
# # for key,value in r.cookies.items():
# #     print(key+";"+value)
# # print(r.text)

# import requests
#
# s  = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# r = s.get("http://httpbin.org/cookies")
# print(r.text)

# import requests
# import logging
#
# logging.captureWarnings(True)
# response = requests.get("https://www.12306.cn",verify=False)
# print(response.status_code)

# import requests
#
# url = 'https://www.12306.cn'
# cafile = 'cacert.pem' # http://curl.haxx.se /ca/cacert.pem
# r = requests.get(url, verify=cafile)
# print(r.status_code)

# import requests
#
# # 代理池
# proxies = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080',
# }
#
# r = requests.get('https://www.taobao.com',proxies=proxies)
# print(r.status_code)

# import requests
# from requests.auth import HTTPBasicAuth
#
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)

# import requests
# from requests_oauthlib import OAuth1
#
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url,auth=auth)


from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name':'angle',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)