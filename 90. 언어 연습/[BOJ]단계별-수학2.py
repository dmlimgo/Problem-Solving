#2581 소수
M = int(input())
N = int(input())

minSosu = 0
hapSosu = 0
sosu = [1] * (N+1)
for i in range(2, N+1):
    if sosu[i]:
        if M <= i:
            hapSosu += i
            if minSosu == 0:
                minSosu = i
        for j in range(2, N//i+1):
            sosu[i*j] = 0
if hapSosu == 0:
    print(-1)
else:
    print(hapSosu)
    print(minSosu)