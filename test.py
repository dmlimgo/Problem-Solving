import time

start = time.time()
a = [i for i in range(10000000)]

print(time.time()-start)

start = time.time()
a = [0] * 10000000
for i in range(10000000):
    a[i] = i
print(time.time()-start)