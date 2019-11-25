import sys
input = sys.stdin.readline

answer = 0

def find(g):
    if g == gates[g]:
        if g:
            gates[g] = g-1
            return 0
        else:
            return -1
    p = find(gates[g])
    if p:
        gates[g] = p
        return p
    else:
        return -1

def dock(gi):
    global answer
    g = gi
    while g >= 0:
        p = find(g)
        if p:
            g = p-1
        else:
            answer += 1
            return 1
    return 0


G = int(input())
P = int(input())

gates = [i for i in range(G+1)]
print(gates)
for i in range(P):
    gi = int(input())
    docked = dock(gi)
    print(gates)
    if not docked:
        break
print(answer)