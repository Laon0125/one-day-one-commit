#107페이지 맨마지막문단 
f = open('./Day1118/data/two_times_table.txt', mode='w' )
for num in range(1,6):
    format_string = '2 * {0} = {1}\n'.format(num, 2*num)
    f.write(format_string) #기록저장 

print('two_times_table.txt 저장 성공')
f.close()

#110page
import time
print('two_times_table.txt파일읽기')
time.sleep(1)
file = open('./Day1118/data/two_times_table.txt', mode='r' )
# print(file.readlines()) #['2 * 1 = 2\n', '2 * 2 = 4\n', '2 * 3 = 6\n', '2 * 4 = 8\n', '2 * 5 = 10\n']
# print()
for line in file.readlines():
    print(line, end='')
file.close()
print()