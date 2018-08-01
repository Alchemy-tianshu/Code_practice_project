import http.cookiejar,urllib.request

# 声明一个CookieJar对象
cookie = http.cookiejar.CookieJar()
# 构建一个handler
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建一个opener
opener = urllib.request.build_opener(handler)
# 打开网站
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)