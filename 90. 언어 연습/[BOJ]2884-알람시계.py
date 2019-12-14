H, M = map(int, input().split())
h, m = divmod(60*H+M-45, 60)
if h < 0:
    print(h+24, m)
else:
    print(h, m)