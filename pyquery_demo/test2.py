html = '''
<div id="container">
    <ul class="list">
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
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

# from pyquery import PyQuery as pq
#
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# list_itmes = items.find('li')
# print(type(list_itmes))
# print(list_itmes)


from pyquery import PyQuery as pq

items = pq(html)
lis = items.children('.list .active')
print(type(lis))
print(lis)
