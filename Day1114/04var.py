# 04var.py
# 변수초기화
# 1 * 2 * 3 * 4 * 5 * hap = 15
su, hap = 0, 0

print() # 라인 대행

su = 1; print(su, '*', end =' '); hap = su
su = su + 1; print(su, '*', end =' '); hap = hap * su 
su = su + 1; print(su, '*', end =' '); hap = hap * su
su = su + 1; print(su, '*', end =' '); hap = hap * su
su = su + 1; print(su, end =' '); hap = hap * su

print ("합계 = ", hap)