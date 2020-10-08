import re
#phoneregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#no = phoneregex.search("my number is 889-889-9805")
#print(no.group())


batregex = re.compile(r'Bat(man|mobile|ball)')
text = batregex.search('I like Batman')
print(text.group())
