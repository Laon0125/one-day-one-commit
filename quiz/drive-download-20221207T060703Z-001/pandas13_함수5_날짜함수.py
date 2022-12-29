'''

    날짜 데이터 처리

    1. 파이썬
        from datetime import datetime

    2. pandas
'''

# 1. 파이썬
from datetime import datetime

print(dir(datetime))
'''
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', 
'__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', 
'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 
'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 
'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 
'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 
'strptime', 'time', 
'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 
'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 
'weekday', 'year']
'''

print('1.현재날짜:', datetime.now())
print('1.현재날짜:', datetime.today())

print('2. 년도:', datetime.today().year)
print('2. 월:', datetime.today().month)
print('2. 일:', datetime.today().day)
print('2. 시:', datetime.today().hour)
print('2. 분:', datetime.today().minute)
print('2. 초:', datetime.today().second)
print('2. 밀리초:', datetime.today().microsecond)


new_date = datetime(2022,12,7)
date_dict = {
    'year':2022,
    'month':11,
    'day':24
}

new_date = datetime(**date_dict)
print(new_date)

# 문자열 --> 날짜로
new_date = datetime.strptime("2022-12-8", "%Y-%m-%d")
print(new_date, type(new_date))


new_date = datetime.strptime("20221208", "%Y%m%d")
print(new_date)

# 날짜 --> 문자열
new_date = datetime.strptime("20221208", "%Y%m%d")

str_date = new_date.strftime('%Y년,%m월,%d일')
print(str_date)