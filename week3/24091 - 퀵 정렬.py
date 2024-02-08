import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0

def quick_sort(list, left, right):
    if left < right:
        q = partition(list, left, right)
        quick_sort(A, left, q - 1)
        quick_sort(A, q + 1, right)

def partition(list, left, right):
    global count
    x = list[right] # 피벗
    i = left - 1
    for j in range (left, right, 1):
        if list[j] <= x:
            i += 1
            list[i], list[j] = list[j], list[i]
            count += 1
            if count == K:
                print(*list)
                exit()
    if (i + 1 != right):
        list[i + 1], list[right] = list[right], list[i + 1]
        count += 1
        if count == K:
                print(*list)
                exit()
    return i + 1    
quick_sort(A, 0, N-1)
print(-1)