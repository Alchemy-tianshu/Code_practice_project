import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
# \s:空格
# \w:字母及数字、下划线
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())