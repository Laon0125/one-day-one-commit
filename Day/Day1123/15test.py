import numpy as np

a = [ 175, 177, 179, 181, 183]
# 넘피 이용하지 않고 수작업으로 처리
# 첫번쨰 총점, 평균
hap = 0
avg = 0
for i in a :
    hap += i 

avg = hap / 5
print('일반총점 = ', hap)
print('일반평균 = ', avg)

# 두번쨰 편차
    # 편차 = 4 + 2 + 0 + (-2) + (-4) = 0 ....?
    # 4*4 16, 2*2 4, 0*0 0, (-2)*(-2) 4, (-4)*(-4) 16
    # 40 / 5 = 분산값
def deviation(num_List) :
    counter = 0
    list_for_return = list()
    for x in num_List :
        dev_Num = avg - num_List[counter]
        #print (dev_Num) <-- testing purpose
        list_for_return.append(dev_Num)
        counter += 1
    return list_for_return

# 3번째 분산 = 편차의 제곱 / 인원 np.var()     
def variance(num_list) :
    counter = 0
    squar_num = 0 
    sqr_Sum = 0
    var_Num = 0
    for y in num_list :
        squar_num = y * y
        sqr_Sum += squar_num
        counter += 1
    var_Num = sqr_Sum/(counter)
    return var_Num

 # 4번쨰 표준편차 np.std()       
def standard_dev (x) :
    y = x**(0.5)
    return y
        
#testing
print(deviation(a))
z = deviation(a)
print (variance(z))
x = variance(z)
print ( standard_dev(x))
