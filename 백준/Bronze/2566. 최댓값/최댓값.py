res1, res2 = 0, [0, 0]
for i in range(9):
    tmp = list(map(int, input().split()))
    idx, num = tmp.index(max(tmp)), max(tmp)
    if num > res1:
        res1, res2 = num, [i, idx]
res2[0] += 1
res2[1] += 1
print(res1)
print(*res2)