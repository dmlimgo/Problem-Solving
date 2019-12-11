import sys
input = sys.stdin.readline

nums = [1 for _ in range(246913)]
for i in range(2, 246913):
    if nums[i]:
        for j in range(2, 246912//i+1):
            nums[i*j] = 0
n = int(input())
while n:
    cnt = 0
    for i in range(n+1, 2*n+1):
        if nums[i]:
            cnt += 1
    print(cnt)
    n = int(input())