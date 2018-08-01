import re

content = 'Hello 123456789 World'
result = re.match('^Hello.*(\d+).*World$', content)
print(result)
print(result.group(1))

result = re.match('^Hello.*?(\d+).*World$', content)
print(result)
print(result.group(1))