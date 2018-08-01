# from lxml import etree
#
# html = etree.parse('test.html',etree.HTMLParser())
# # result = html.xpath('//li/a')
# result = html.xpath('//li//a')
# print(result)


# from lxml import etree
#
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)


# from lxml import etree
#
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)


# from lxml import etree
#
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)


# from lxml import etree
#
# html = etree.parse('test.html',etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)


# from lxml import etree
#
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li")]/a/text()')
# print(result)


from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)