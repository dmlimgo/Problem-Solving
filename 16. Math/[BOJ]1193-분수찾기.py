X = int(input())

n = (-1 + (1+8*X)**0.5)/2
if n == int(n):
    n = int(n)
    a = 1
    hap = n+1
    b = hap - a
    if hap // 2:
        print(f'{a}/{b}')
    else:
        print(f'{b}/{a}')
else:
    n = int(n)
    a = int(X - n*(n+1)//2)
    hap = n+2
    b = hap - a
    if hap // 2:
        print(f'{b}/{a}')
    else:
        print(f'{a}/{b}')
