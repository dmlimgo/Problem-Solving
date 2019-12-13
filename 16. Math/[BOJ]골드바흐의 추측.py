import sys
input = sys.stdin.readline

sosu = []
nums = [1 for i in range(10001)]
nums[0] = nums[1] = 0
for i in range(2, 10001):
    if nums[i]:
        sosu.append(i)
        for j in range(2, 10000//i+1):
            nums[i*j] = 0
# print(sosu)
# print(len(sosu))
T = int(input())
for tc in range(T):
    n = int(input())
    L, R = 0, 1228
    switch = 0
    for i in range(1229):
        for j in range(1229):
            if sosu[i] + sosu[j] == n and (abs(sosu[i] - sosu[j])<abs(L-R)):
                L, R = sosu[i], sosu[j]
    print(L, R)