from urllib import request,error

try:
    response = request.urlopen('http://www.runoob.com/python1.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')