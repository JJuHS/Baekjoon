n, k = map(int, input().split())
arr = []
for i in range(n):
    a, b, c, d = map(str, input().split())
    arr.append([-int(c), int(d), a, b])
arr.sort(key=lambda x: (x[0], x[1]))

cnt, univ = 0, []
for a, b, c, d in arr:
    if c in univ:
        continue
    print(d)
    cnt += 1
    univ.append(c)
    if cnt == k:
        break