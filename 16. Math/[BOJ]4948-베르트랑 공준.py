import sys
input = sys.stdin.readline

nums = [1 for _ in range(246913)]
nums[0] = nums[1] = 0
cnt = 0
for i in range(2, 246913):
    if nums[i]:
        cnt += 1
        nums[i] = cnt
        for j in range(2, 246912//i+1):
            nums[i*j] = 0
    else:
        nums[i] = cnt

n = int(input())
while n:
    print(nums[2*n]-nums[n])
    n = int(input())