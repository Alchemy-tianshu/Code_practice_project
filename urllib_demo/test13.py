from urllib import request,error

try:
    response = request.urlopen('http://www.runoob.com/python1.html')
except error.URLError as e:
    print(e.reason)