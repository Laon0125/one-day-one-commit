import re

phone = '''
 010-7100-1234 kim
 010-9200-9876 lee
 010-5400-5432 aws
'''

retA = re.sub('-[0-9]{4}-','-****-',phone)
print(retA)

retB = re.sub('[0-9]{3}-[0-9]{4}-[0-9]{4}','***-****-****',phone)
print(retB)


retC = re.sub('[0-9]{3}-[0-9]{4}-','***-****-',phone)
print(retC)



