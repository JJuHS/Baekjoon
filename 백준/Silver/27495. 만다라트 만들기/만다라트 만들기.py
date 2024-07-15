arr = [input().split() for _ in range(9)]

res = []
def sol(a, b):
    tmp = []
    for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        tmp.append(arr[x + a][y + b])
    res.append([arr[a][b], sorted(tmp)])

for i in [1, 4, 7]:
    for j in [1, 4, 7]:
        if i == j == 4:
            continue
        sol(i, j)

res.sort()
for i in range(8):
    print(f'#{i + 1}. {res[i][0]}')
    for j in range(8):
        print(f'#{i + 1}-{j + 1}. {res[i][1][j]}')