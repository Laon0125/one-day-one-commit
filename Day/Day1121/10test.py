my = [ 'LG.py', 'facebook.h', 'game.c', 'define.h']

for data in my :
    a = data.split(".")
    # print (a)
    if a [1] == "gif" or a [1] =='py' :
        print(data, end=" ")
    else :
        print("업로드할수없습니다")