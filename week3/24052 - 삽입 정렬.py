import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
def insertion_sort(list):
    global count
    for i in range(1, N, 1): # i = 1, 2, ..., N
        loc = i - 1
        newItem = A[i]
        while 0 <= loc and newItem < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
            count += 1            
            if count == K:
                print(*A)
                exit()

        if loc + 1 != i:
            A[loc + 1] = newItem
            count += 1
            if count == K:
                print(*A)
                exit()  
insertion_sort(A)
print(-1)