res = [0] * 11001
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for n in range(0, 10):
                now = 1001*i + 101*j + 11*k + 2*n
                res[now] = 1
for i in range(1, 10001):
    if res[i]:continue
    print(i)
                