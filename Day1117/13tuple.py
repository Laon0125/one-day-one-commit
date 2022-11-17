# 13tuple.py

pos = (
    '양재',
    36.32423,
    127.123123, 
    "시청", 
    37.123145, 
    126.941231
    )

movie = ('오징어게임', '블랙아담', '유미의세포')

#문제 movie 튜플에 내용추가

print(movie)
movie_list = list(movie)
movie_list.append("abc")
movie = tuple(movie_list)
print(movie)