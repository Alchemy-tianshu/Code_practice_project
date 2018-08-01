import re

content = 'Hello123World'
pattern = '\d+'
print("原内容:"+content)
content = re.sub(pattern,'',content)
print("新内容:"+content)
