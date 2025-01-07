import os, io, __pypy__

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
_, m = map(int, input().split())
res = __pypy__.builders.StringBuilder()
res_next = [0]*1000001
res_prev = [0]*1000001

initial_station = list(map(int, input().split()))
initial_station.append(initial_station[0])

for i in range(len(initial_station) - 1):
    res_next[initial_station[i]] = initial_station[i + 1]
    res_prev[initial_station[i + 1]] = initial_station[i]

for _ in range(m):
    cmd, *num = input().split()
    if cmd == b'BN':
        i, j = int(num[0]), int(num[1])
        next = res_next[i]
        res.append(str(next) + '\n')
        res_next[i] = j
        res_next[j] = next
        res_prev[j] = i
        res_prev[next] = j
    elif cmd == b'BP':
        i, j = int(num[0]), int(num[1])
        prev = res_prev[i]
        res.append(str(prev) + '\n')
        res_prev[i] = j
        res_prev[j] = prev
        res_next[j] = i
        res_next[prev] = j
    elif cmd == b'CN':
        i = int(num[0])
        next = res_next[i]
        res.append(str(next) + '\n')
        res_next[i] = res_next[next]
        res_prev[res_next[next]] = i
    else:
        i = int(num[0])
        prev = res_prev[i]
        res.append(str(prev) + '\n')
        res_prev[i] = res_prev[prev]
        res_next[res_prev[prev]] = i
    
os.write(1, res.build().encode())