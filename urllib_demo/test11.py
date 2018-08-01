import urllib.request,http.cookiejar

filename = "cookies.txt"
# 如果存储为文本格式，需要用到MozillaCookieJar
# cookies = http.cookiejar.MozillaCookieJar(filename)
cookies = http.cookiejar.LWPCookieJar(filename)
# 构建一个handler
handler = urllib.request.HTTPCookieProcessor(cookies)
# 构建一个opener
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookies.save(ignore_discard=True,ignore_expires=True)