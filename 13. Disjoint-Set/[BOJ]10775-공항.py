import sys
input = sys.stdin.readline

answer = 0

# def find(g):
#     if g == gates[g]:
#         if g:
#             gates[g] = g-1
#             return 0
#         else:
#             return -1
#     p = find(gates[g])
#     if p:
#         gates[g] = p
#         return p
#     else:
#         return -1
def find(g):
    if g == gates[g]:
        return g
    gates[g] = find(gates[g])
    return gates[g]

def docking(g):
    global answer
    if g == gates[g]:
        gates[g] = g-1
        answer += 1
        return 1
    else:
        root = find(g)
        if root:
            gates[g] = root - 1
        return 0


G = int(input())
P = int(input())

gates = [i for i in range(G+1)]
for i in range(P):
    g = int(input())
    docked = docking(g)
    print('gates', i, gates)
    if not docked:
        break
print(answer)