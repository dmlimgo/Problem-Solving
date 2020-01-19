from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    s = deque([])
    data = input().strip('\n')
    vps = True
    for d in data:
        if d == '(':
            s.append('(')
        else:
            if s and s[-1] == '(':
                s.pop()
            else:
                vps = False
                break
    if vps and len(s) == 0:
        print('YES')
    else:
        print('NO')
