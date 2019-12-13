import sys
input = sys.stdin.readline

nums = [1 for i in range(10001)]
parent = [0 for i in range(10001)]
nums[0] = nums[1] = 0
before = -1
for i in range(2, 10001):
    if nums[i]:
        parent[i] = before
        before = i
        for j in range(2, 10000//i+1):
            nums[i*j] = 0
    else:
        parent[i] = before

T = int(input())
for tc in range(T):
    n = int(input())
    l = n//2
    while True:
        if nums[l] and nums[n-l]:
            print(l, n-l)
            break
        else:
            l = parent[l]
