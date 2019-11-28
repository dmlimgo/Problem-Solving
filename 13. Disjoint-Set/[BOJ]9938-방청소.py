import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a, b):
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

N, L = map(int, input().split())
parent = [i for i in range(L+1)]
for i in range(N):
    a, b = map(int, input().split())
    find(a, b)
    print([i for i in range(0, 11)])
    print(parent)
