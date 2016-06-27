import re
x = 'We just oreceived $10.156780 for cookies. '
print x
y = re.findall('^\s[aeiou]+',x)
print y
