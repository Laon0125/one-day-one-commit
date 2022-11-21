#myFileload.py
#107페이지 맨마지막문단 
f = open('./Day1118/data/my.txt', mode='w' )
for num in range(1,6):
    format_string = '2 * {0} = {1}\n'.format(num, 2*num)
    f.write(format_string) #기록저장 

print('two_times_table.txt 저장 성공, 11월 21일 월요일 9시 43분 저장처리')
f.close()
