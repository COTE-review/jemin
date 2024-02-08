import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
def bubble_sort (list):      #버블 정렬 함수 선언
    count = 0
    for last in range (N - 1, 0, -1):     # last : N-1, N-2, ..., 0
        for i in range(0, last, 1): # i : 1, 2, ..., last - 1
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                count += 1
                if count == K:
                    print(list[i], list[i+1])
                    break
    if count < K:
        print(-1)
bubble_sort(A)
