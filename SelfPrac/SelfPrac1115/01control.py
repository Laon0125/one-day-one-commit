# 01control.py
# 입력받은 수가 양수인지 음수인지 판별

a = int(input('Enter a number >>>'))

if a > 0 :
    print(a, " is a positive number!")

elif a < 0 :
    print(a, " is a negative number!")

else :
    print(a, " is positive nor negative!")