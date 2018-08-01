html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# from pyquery import PyQuery as pq
#
# doc = pq(html)
# print(doc('li'))

# from pyquery import PyQuery as pq
# import requests
#
# # doc = pq(url='https://github.com/CoderAngle')
# doc = pq(requests.get('https://github.com/CoderAngle').text)
# print(doc('title'))

# coding:utf-8
from pyquery import PyQuery as pq

doc = pq(filename='test.html')
print(doc('li'))