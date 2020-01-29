import sys
input = sys.stdin.readline

while True:
    data = input()
    if data.strip() == '0 0 0': break
    a, b, c = sorted(list(map(int, data.split())))
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")

