import re

msg = 'my phone number is 9611-5696, my best friend number is 8280-1079'

reg = re.compile(r'\d\d\d\d-\d\d\d\d')

mo = reg.search(msg)
all = reg.findall(msg)

print(mo.group())
print(all)