import sys
input = sys.stdin.readline

def find(u):
    if parent[u] < 0:
        return u
    parent[u] = find(parent[u])
    return parent[u]
    # return find(parent[u])

def merge(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        parent[u] += parent[v]
        parent[v] = u

T = int(input())
for tc in range(T):
    F = int(input())
    parent = [-1 for i in range(F+1)]
    friend = {}
    index = 0
    for i in range(F):
        a, b = input().split()
        if a not in friend:
            friend[a] = index
            index += 1
        if b not in friend:
            friend[b] = index
            index += 1
        merge(friend[a], friend[b])
        print(parent[find(friend[a])] * (-1))