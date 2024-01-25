#import sys
#input = sys.stdin.readline
i = 0
N = int(input())
N_1 = set(input().split())    #존재 여부만 확인할 것이기 때문에, 같은 수는 1개만 존재해도 가능
                              #비교해야되는 N_1의 길이를 줄이기 위해  set 사용
M = int(input())
M_1 = input().split()

while(i < M):
    if M_1[i] in N_1:
        print(1)
    else:
        print(0)
    i += 1


"""
#import sys
#input = sys.stdin.readline
i = 0
N = int(input())
N_1 = list(map(int, input().split()))
M = int(input())
M_1 = list(map(int, input().split()))

while(i < M):
    if M_1[i] in N_1:
        print(1)
    else:
        print(0)
    i += 1
"""

"""
#import sys
#input = sys.stdin.readline
i = 0
N = int(input())
N_1 = input().split()
M = int(input())
M_1 = input().split()

while(i < M):
    if M_1[i] in N_1:
        print(1)
    else:
        print(0)
    i += 1

"""

#아래 2개 코드 모두 시간초과