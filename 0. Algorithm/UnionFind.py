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
    # level 사용시
    # if level[u] > level[v]:
    #     u, v = v, u
    parent[u] = v
    # level 사용시
    # if level[u] == level[v]:
    #     level[v] += 1

n = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
