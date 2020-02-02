import sys
input = sys.stdin.readline

n = int(input())
s = input()

print(s.count('R') + s.count('L') + 1)