a = list(range(1, 11))                      # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 생성
result = [y*3 for y in a if y%2 == 0]       # a 내에서 x%2 == 0 인 x들만 3배 하라는 뜻
print(result)                               # result 출력
