import sys
input = sys.stdin.readline

matrix = [input().split() for _ in range(5)]

for row in range(5):
    if '1' in matrix[row]:
        x = matrix[row].index('1')
        y = row
        break

print(abs(x-2) + abs(y-2))

        