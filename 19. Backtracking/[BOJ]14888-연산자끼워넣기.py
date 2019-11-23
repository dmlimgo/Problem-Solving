N = int(input())
numbers = list(map(int, input().split()))
hap, cha, gob, nan = map(int, input().split())

max_val = -1000000001
min_val = 1000000001
def dfs(pos, res, hap, cha, gob, nan):
    global max_val, min_val
    if pos == N-1:
        if res > max_val:
            max_val = res
        if res < min_val:
            min_val = res
        return
    if hap: dfs(pos+1, res+numbers[pos+1], hap-1, cha, gob, nan)
    if cha: dfs(pos+1, res-numbers[pos+1], hap, cha-1, gob, nan)
    if gob: dfs(pos+1, res*numbers[pos+1], hap, cha, gob-1, nan)
    if nan: dfs(pos+1, int(res/numbers[pos+1]), hap, cha, gob, nan-1)


dfs(0, numbers[0], hap, cha, gob, nan)
print(max_val)
print(min_val)
