from urllib.parse import urlparse

# result = urlparse("https://www.google.com.hk/search;user?q=python#content")
# print(type(result),result,sep='\n')

# result = urlparse("http://www.google.com.hk/search;user?q=python#content",scheme="https")

# result = urlparse("https://www.google.com.hk/webhp#content",allow_fragments=False)
# print(result)

# from urllib.parse import urlparse
#
# result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
# print(result.scheme, result[0], result.netloc, result[1], sep='\n')

# from urllib.parse import urlunparse
# data = ['http', 'www.google.com', 'index.html', 'name', 'q=6', 'comment']
# print(urlunparse(data))

# from urllib.parse import  urlsplit
# result = urlsplit("https://www.google.com.hk/webhp#content")
# print(result.scheme,result[0])

# from urllib.parse import urlunsplit
# data = ['http', 'www.google.com', 'index.html', 'q=6', 'comment']
# print(urlunsplit(data))

# from urllib.parse import urlencode
#
# params = {
#     'wd':'python',
# }
# base_url = 'https://www.baidu.com/s?'
# url = base_url + urlencode(params)
# print(url)

# from urllib.parse import parse_qsl
#
# query = '''f=json&mock=&uin=777&key=777&pass_ticket=nFLy3qzW6g8xVh%25252FRdSuoEMZn%25252BYrRjEh0fsybociYtgE%25253D&wxtoken=777&devicetype=android-26&clientversion=26060739&appmsg_token=966_3pMS7R2ZHEtCjbLZ3O0EDgaTpZ9B-N7GrMG3lOqeNFz9EH9p3dcgPHSiCjE~&x5=1&f=json'''
# print(parse_qsl(query))

# from urllib.parse import  quote
#
# wd = "猫"
# url = "https://www.baidu.com/s?wd="+quote(wd)
# print(url)

from urllib.parse import  unquote

url = "https://www.baidu.com/s?wd=%E7%8C%AB"
print(unquote(url))