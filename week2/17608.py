#최적화 넣은 버전
nofstick = int(input())
stick = []
for i in range(nofstick):
    a = int(input())
    stick.append(a)
big = max(stick)
last = stick[-1]
bigindex = len(stick) - stick[::-1].index(max(stick)) - 1
stick = stick[bigindex:]
stick = stick[::-1]
tmp = stick[0]
seenstick = [tmp]
for i in range(len(stick)):    
    if stick[i] > tmp:
        seenstick.append(stick[i])
        tmp = stick[i]
print(len(seenstick))

#최적화 안 넣은 일반 버전
"""
nofstick = int(input())
stick = []
for i in range(nofstick):
    a = int(input())
    stick.append(a)
tmp = stick[-1]
seenstick = [tmp]
for i in range(nofstick - 2, -1, -1):    
    if stick[i] > tmp:
        seenstick.append(stick[i])
        tmp = stick[i]
print(len(seenstick))
"""
#둘 다 시간 복잡도는 O(n)