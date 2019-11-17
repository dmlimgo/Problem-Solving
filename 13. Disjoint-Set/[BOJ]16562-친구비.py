import sys
input = sys.stdin.readline

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        parent[u] = v


N, M, k = map(int, input().split())
friend = list(map(int, input().split()))

parent = [i for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    merge(a, b)

money = {}
total = 0
for i in range(1, N+1):
    root = find(i)
    if root in money:
        if money[root] > friend[i-1]:
            total -= money[root]
            money[root] = friend[i-1]
            total += money[root]
    else:
        money[root] = friend[i-1]
        total += money[root]

if total <= k:
    print(total)
else:
    print("Oh no")

