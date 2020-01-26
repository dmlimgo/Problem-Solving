import sys
input = sys.stdin.readline

def check(diff, amount):
    amount -= 1
    install_i = 0
    for house_i in range(1, N):
        if (house_position[house_i] - house_position[install_i]) >= diff:
            amount -= 1
            install_i = house_i
        if amount == 0:
            break
    if amount == 0:
        return 1
    else:
        return 0


def b_search():
    s = 0
    e = max(house_position) - min(house_position)
    while s <= e:
        m = (s + e)//2
        if check(m, C):
            s = m + 1
        else:
            e = m - 1
    return e

N, C = map(int, input().split())
house_position = sorted([int(input()) for _ in range(N)])
print(b_search())
