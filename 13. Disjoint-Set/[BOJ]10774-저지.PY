import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def sizeToInt(size):
    if size == 'S': return 1
    elif size == 'M': return 2
    elif size == 'L': return 3
    else: return 0

J = int(input())
A = int(input())

judge = {}
for i in range(1, J+1):
    judge[i] = sizeToInt(input().strip('\n'))

cnt = 0
for i in range(A):
    size, num = input().split()
    size = sizeToInt(size)
    num = int(num)
    if judge[num] and judge[num] >= size:
        judge[num] = 0
        cnt += 1
print(cnt)