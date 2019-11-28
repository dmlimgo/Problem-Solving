import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def mergea(a, b):
    while True:
        if a == parent[a]:
            parent[a] = b
            print("LADICA")
            break
        else:
            if parent[a] == -1:
                print("SMECE")
                break
            p = parent[a]
            parent[a] = b
            a = p
            b = -1

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
    while True:
        if n == parent[n]:
            return 1
        elif parent[n] == -1:
            return 0
        else:
            n = parent[n]


N, L = map(int, input().split())
parent = [i for i in range(L+1)]
for i in range(N):
    a, b = map(int, input().split())
    if find(a):
        merge(a, b)
    elif find(b):
        
    print([i for i in range(0, 11)])
    print(parent)
