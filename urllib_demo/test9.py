from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

# 建立代理池
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:5000',
    'https': 'https://127.0.0.1:5000'
})

opener = build_opener(proxy_handler)

try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)