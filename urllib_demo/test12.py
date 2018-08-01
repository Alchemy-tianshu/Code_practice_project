import urllib.request,http.cookiejar

cookies = http.cookiejar.LWPCookieJar()
cookies.load(filename='cookies.txt',ignore_expires=True,ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))
for cookie in cookies:
    print(cookie)