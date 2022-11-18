a = int(input())
b = int(input())
c = int(input())
break_even_point = 0

if c >= b or a < c : 
    print(-1)
else: 
    break_even_point = a/(c-b)
    break_even_point = int(break_even_point) + 1

    if break_even_point <= 0 :
        print (-1)
    elif break_even_point > a/(c-b) :
        print (break_even_point)


