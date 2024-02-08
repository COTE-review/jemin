import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
def selection_sort (list):      #선택 정렬 함수 선언
    count = 0
    for last in range(N-1, 0, -1): # last : N-1, N-2, N-3, ..., 0
        list_1 = list[:last+1]
        x = max(list_1)
        i = list.index(x)      #list[i]가 list[:last+1] 내 최댓값
        if (last != i):
            A[last], A[i] = A[i], A[last]
            count += 1
            if count == K:
                print(A[i], A[last])    
                break
    if count < K:
        print(-1)
selection_sort(A)
