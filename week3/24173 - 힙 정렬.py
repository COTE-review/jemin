"""
import sys
#sys.setrecursionlimit(100000)
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0

def heap_sort(list, n):
    global count
    build_min_heap(list, n)
    for i in range(n, 0, -1):
        list[0], list[i] = list[i], list[0]
        heapify(list, 0, i - 1)

def build_min_heap(list, n):
    for i in range(n//2, -1, -1):
        heapify(list, i, n)

def heapify(list, k, n):
    global count
    left = 2*k
    right = 2*k + 1
    if right <= n:
        if list[left] < list[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return
    
    if (list[smaller] < list[k]):
        list[k], list[smaller] = list[smaller], list[k]
        heapify(list, smaller, n)

heap_sort(A, N - 1)
print(A)
"""
def heap_sort(li, n):
    global count
    build_min_heap(li, n);
    for i in range(n, 1, -1):
        li[1], li[i] = li[i], li[1]
        count += 1
        #print(li)
        if count == K:
            print(li[i], li[1])
            exit()
        heapify(li, 1, i - 1);

def build_min_heap(li, n):
    for i in range(n // 2, 0, -1):
        heapify(li, i, n)

def heapify(li, k, n):
    global count
    left, right = 2 * k, 2 * k + 1
    if right <= n:
        smaller = left if li[left] < li[right] else right
    elif left <= n:
        smaller = left
    else:
        return

    if li[smaller] < li[k]:
        li[k], li[smaller] = li[smaller], li[k]
        count += 1
        #print(li)
        if count == K:
            print(li[k], li[smaller])
            exit()
        heapify(li, smaller, n);

N, K = map(int, input().split())
li = [0] + list(map(int, input().split()))
count = 0
heap_sort(li, N)
print(-1)