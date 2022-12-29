# 01fileWriter.py

#"a"를 쓰면 추가 'w'를 쓰면 덮어쓰기
with open ('abc.txt', 'a', encoding='utf-8') as myfile: 
    name = input('이름입력')
    age = input('나이입력')
    juso = input('주소입력')

    myfile.write(name + '\n')
    myfile.write(age + '\n')
    myfile.write(juso + '\n')

print ("abc.txt파일 저장 성공 10:20")