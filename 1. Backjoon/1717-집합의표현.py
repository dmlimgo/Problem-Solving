import sys

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return
    parent[u] = v

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

for i in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if not c:
        merge(a, b)
    else:
        a = find(a)
        b = find(b)
        if a == b:
            print('yes')
        else:
            print('no')