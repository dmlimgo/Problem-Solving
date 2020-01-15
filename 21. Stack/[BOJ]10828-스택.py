import sys
input = sys.stdin.readline

N = int(input())
s = []
for i in range(N):
    command = input().split()
    if command[0] == 'push':
        s.append(int(command[1]))
    elif command[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(s))
    elif command[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)
    else:
        if s:
            print(s[-1])
        else:
            print(-1)
    # print(s)