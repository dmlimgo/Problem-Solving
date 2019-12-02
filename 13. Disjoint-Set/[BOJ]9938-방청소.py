import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def merge(a, b):
    while True:
        if a == parent[a]:
            parent[a] = b
            break
        p = parent[a]
        parent[a] = b    
        a = p
        b = -1

def find(n):
    init = n
    while True:
        if n == parent[n]:
            return 1
        elif parent[n] == -1 or parent[n] == init:
            return 0
        else:
            n = parent[n]


N, L = map(int, input().split())
parent = [i for i in range(L+1)]
for i in range(N):
    a, b = map(int, input().split())
    if find(a):
        merge(a, b)
        print("LADICA")
    elif find(b):
        merge(b, -1)
        print("LADICA")
    else:
        print("SMECE")        
    print([i for i in range(0, L+1)])
    print(parent)
