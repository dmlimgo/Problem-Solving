numbers = [1 for _ in range(1001)]
numbers[1] = 0
for i in range(2, 1001):
    if numbers[i]:
        for j in range(2, (1000//i)+1):
            numbers[i*j] = 0

N = int(input())
M = list(map(int, input().split()))
cnt = 0
for m in M:
    if numbers[m]:
        cnt += 1
print(cnt)