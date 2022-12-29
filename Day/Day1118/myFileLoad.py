f = open('./Day1118/data/two_times_table.txt', mode='r' )
# for num in range(1,6):
#     print(f.readlines())
#     print()

for line in f.readlines() :
    print (line, end='')

print('two_times_table.txt 저장 성공, 11월 21일 월요일 9시 43분 저장처리')
f.close()
