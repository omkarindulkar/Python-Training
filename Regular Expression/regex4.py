#   ? (0 or 1)
import re
# batregex = re.compile(r'bat(wo)?man')
# text = batregex.search("I like batman")
# print(text.group())

#   * (0 or more)
# batregex = re.compile(r'bat(wo)*man')
# text = batregex.search("I like batwowoman")
# print(text.group())

#   + (1 or more)
# batregex = re.compile(r'bat(wo)+man')
# text = batregex.search("I like batwoman")
# print(text.group())

#   {1,5}
# batregex = re.compile(r'bat(wo){2,4}man')
# text = batregex.search("I like batwowoman")
# print(text.group())

# numregex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# num = numregex.search("my phone numbers are 889-889-9805,777-122-1055,932-9122")
# print(num.group())

#Greedy and (?)Non Greedy
numregex = re.compile(r'\d{4,5}')
no = numregex.search(" my fav no is 123456789")
print(no.group())


