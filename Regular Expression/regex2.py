import re
message = "call me on 888-889-9905 or 889-888-1055"
phregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
num = phregex.search(message)
print(phregex.findall(message))
print(num.group())