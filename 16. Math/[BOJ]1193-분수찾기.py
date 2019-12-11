X = int(input())
n = (-1 + (1+8*X)**0.5)/2
if n == int(n):
    n = int(n)
    a = 1
    b = n    
else:
    n = int(n)
    a = int(X - n*(n+1)//2)
    b = n+2 - a
if n % 2:
    print(f'{a}/{b}')
else:
    print(f'{b}/{a}')
