import re
# pregex = re.compile(r'\d\d\d')
# print(pregex.findall("my name is 567 and call me on 889"))

# pregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# print(pregex.findall("my name is 567-885-0021 and call me on 889-999-5555"))

# pregex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
# print(pregex.findall("my name is 567-885-0021 and call me on 889-999-5555"))

#12 drummers drumming, 11 pipers pipping...
# xamreg = re.compile(r'\d+\s\w+')
# print(xamreg.findall("12 drummers drumming, 11 pipers pipping..."))

# vovelreg = re.compile(r'[aeiou]')
# print(vovelreg.findall("12 drummers drumming, 11 pipers pipping..."))

vovelreg = re.compile(r'[^aeiou]')
print(vovelreg.findall("drummersdrummingpiperspipping"))