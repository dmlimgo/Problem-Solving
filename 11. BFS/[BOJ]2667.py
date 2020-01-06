import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = list(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b):
    cnt = 1
    arr[b][a] = '0'
    q = deque([])
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                continue
            if arr[ny][nx] == '1':
                cnt += 1
                arr[ny][nx] = '0'
                q.append((nx, ny))
    return cnt

total = []
x, y = 0, 0
while (x != 0) or (y != N):
    if arr[y][x] == '1':
        total.append(bfs(x, y))
    x += 1
    if x == N:
        x, y = 0, y+1

total.sort()
print(len(total))
for home_count in total:
    print(home_count)