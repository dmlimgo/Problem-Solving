def find(u):
    '''
    u의 root를 찾는 함수
    u부터 root까지의 모든 요소의 parent는 root가 됌 (level 2로 통일)
    '''
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    '''
    u와 v를 합치는 함수

    '''
    u = find(u)
    v = find(v)
    if u == v:
        return
    parent[v] = u
    
    

n = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
print(parent)
for i in range(1, n+1):
    find(i)
print(parent)


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
    if level[u] > level[v]:
        u, v = v, u
    parent[u] = v
    if level[u] == level[v]:
        level[v] += 1

parent = [0] * 201
level = [0] * 201
N = int(input())
M = int(input())
arr = [0 for _ in range(N+1)]

for i in range(1, N+1):
    arr[i] = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    parent[i] = i
    level[i] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if j > i and arr[i][j]:
            merge(i, j)

check = True
val = list(map(int, input().split()))

u = find(val[0])
for i in range(M-1):
    if u != find(val[i]):
        check = False
        break

if check:
    print("YES")
else:
    print("NO")