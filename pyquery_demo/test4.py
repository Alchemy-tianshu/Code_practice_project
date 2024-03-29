# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
#
# from pyquery import  PyQuery as pq
#
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class("active")
# print(li)



# html = '''
# <ul class="list">
#      <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# </ul>
# '''
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name','link')
# print(li)
# li.text('chaned item')
# print(li)
# li.html('<span>changed item</span')
# print(li)



# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''
#
# from pyquery import PyQuery as pq
#
# doc = pq(html)
# wrap = doc('.wrap')
# wrap.find('p').remove()
# print(wrap.text())