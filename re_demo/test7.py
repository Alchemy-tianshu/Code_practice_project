import re

content1 = '2018-7-15 12:00'
content2 = '2018-7-17 12:55'
content3 = '2018-7-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
content1 = re.sub(pattern,'',content1)
content2= re.sub(pattern,'',content2)
content3 = re.sub(pattern,'',content3)
print(content1,content2,content3,sep='\n')

