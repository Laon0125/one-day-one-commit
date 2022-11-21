#03fileRead

with open ('abc.txt', 'r', encoding='utf-8') as myfile:
    #data=myfile.read()

    for line in myfile.readlines() :

        print(line, end = "")
   