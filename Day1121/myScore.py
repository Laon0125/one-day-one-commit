# 리턴값 4개 매개인자 2개
def my_Score_Data(x,y):
    name = "jinwoo"
    
    arg = x + y
    
    average = arg / 2  

    if average >= 70 :
        message = "축 합격"
    else :
        message = "재시험"
    
    return (name, arg, average, message)

kor = 40
eng = 80

print(my_Score_Data(kor, eng))