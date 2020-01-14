N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)][::-1]
# print(arr)
cnt = 0
for danwi in arr:
    if danwi > K:
        continue
    cnt += K // danwi
    K %= danwi
print(cnt)