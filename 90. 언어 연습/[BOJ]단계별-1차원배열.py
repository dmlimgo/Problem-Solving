#3052 나머지
arr = []
for i in range(10):
    n = int(input())%42
    if n not in arr:
        arr.append(n)
print(len(arr))


#2562 최댓값
# maxVal= 0
# maxIndex = 0
# for i in range(9):
#     n = int(input())
#     if maxVal < n:
#         maxVal = n
#         maxIndex = i+1
# print(maxVal)
# print(maxIndex)
