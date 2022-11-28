import re

s ='Apple is big apple company and apple is very delicious'
k = re.compile('apple', re.I) #대소문자무시하고 검색
print(k.findall(s))
print()

n = re.compile('apple') #소문자만 검색
print(n.findall(s))