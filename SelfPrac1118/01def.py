#binary search 방법으로 검색 알고리즘 만들기
numbers=list(range(1,12))
N=len(numbers)
search=int(input("찾으려는 숫자를 입력하세요:"))
TorF=False
f_index=0
l_index=N-1
mid=0
circle=0
while f_index<=l_index:
  circle+=1
  mid=int((f_index+l_index)/2)
  if numbers[mid]==search:
    TorF=True; index=mid; break;
  if numbers[mid]>search:
    l_index=mid-1
  else:
    f_index=mid+1
if TorF:
  print(f"찾으려는 값은 {search}이고, 해당 값은 {index}번 인덱스에 있습니다")
  print(f"해당 값은 {circle}회전만에 찾았습니다")
else:
  print(f"찾으려는 값 {search}를 찾지 못했습니다")