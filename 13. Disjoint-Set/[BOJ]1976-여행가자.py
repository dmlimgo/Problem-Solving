import sys

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


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = [i for i in range(N)]

for i in range(N):
    info = sys.stdin.readline().split()
    for j in range(i+1, N):
        if info[j] == '1':
            merge(i, j)

plan = sys.stdin.readline().split()
start = find(int(plan[0])-1)
for i in plan:
    if start != find(int(i)-1):
        start = -1
        break
if start > -1:
    print('YES')
else:
    print('NO')