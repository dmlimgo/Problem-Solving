x, y, w, h = map(int, input().split())
a = w-x if w//2 < x else x
b = h-y if h//2 < y else y
print(a if a < b else b)