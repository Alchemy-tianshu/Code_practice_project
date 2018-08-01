from urllib import request,parse

url = 'http://httpbin.org/post'
# 伪造请求头
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
# 构造参数
dict = {
    'name':"angle",
}
# 转换为字节流
data = bytes(parse.urlencode(dict),encoding='utf-8')
# req = request.Request(url=url,data=data,headers=headers,method='POST')
req = request.Request(url=url,data=data,method='POST')
req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))