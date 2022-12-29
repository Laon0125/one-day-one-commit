import random
import time 

noodle_list = ['너구리', '신라면', '진라면', '안성탕면', '왕뚜껑', '김치라면']
print (random.choice(noodle_list))
print ("-"*70)
time.sleep(1)

print (random.sample(noodle_list, 2))
print (random.sample(noodle_list,len(noodle_list)))
print ("-"*70)
time.sleep(1)

my_list = [11,22,33,44,55]
print(my_list)
random.shuffle(my_list)
print(my_list)