html='''
<div class="panel">
    <div class="panel-body">
        <a class='element'>Hello, this is a link</a>
        <a class='element'>Hello, this is a link, too</a>
    </div>
</div>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')
print(soup.find(name='a'))
print(soup.find(attrs={'class':'element'}))
print(soup.find(class_='element'))
print(type(soup.find(name='a')))

# import re
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(html,'lxml')
# # 查询文本包含有link的文本
# print(soup.find_all(text=re.compile('link')))