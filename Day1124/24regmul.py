import re

s = '''Gee Gee Gee
가을 하늘 #^#^@^#
봄spring  234235
겨울바다
'''

#c = re.compile('^.+', re.M)
c = re.compile('^\w', re.M)
#c = re.compile('^\w+', re.M)

print(c)
print(c.findall(s))