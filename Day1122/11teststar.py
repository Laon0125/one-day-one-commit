
for a in range(0,6,1):      #큰회전 6바퀴  첫번째 a=0 큰바퀴돌때  b작은바퀴은 0부터시작,a까지0
    for b in range(0,a,1):  #a=0, b범위(0,0) 처리못함  a=1,b범위(0,1)처리
        print("★ ", end=' ')
    print(); #한줄단위로 엔터라인개행


print()
for x in range(5,0,-1): #큰회전문 5바퀴  x=5, 작은회전 0부터5회앞까지 
    for y in range(0, x ,1):
        print('🎍', end =' ')
    print()


'''
for a in range(5):
    for b in range( ):
★  
★  ★  
★  ★  ★  
★  ★  ★  ★  
★  ★  ★  ★  ★ 

print()
for x in range(5):
    for y in range( ):

★ ★ ★ ★ ★ 
★ ★ ★ ★ 
★ ★ ★ 
★ ★ 
★ 
'''