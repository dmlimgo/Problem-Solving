import sys
input = sys.stdin.readline

def bs(n):
    s = 0
    e = N-1
    while s <= e:
        m = (s + e)//2
        if arr[m] == n:
            return 1
        elif arr[m] < n:
            s = m + 1
        else:
            e = m - 1
    return 0

N = int(input())
arr = sorted(list(map(int, input().split())))

M = int(input())
nums = list(map(int, input().split()))
for i in nums:
    print(bs(i))
