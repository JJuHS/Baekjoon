n = int(input())

cnt = 0
for num in range(1, n + 1):
    if num < 100:
        cnt += 1
    else:
        tmp = list(map(int, str(num)))
        s = len(tmp)
        for j in range(s - 2):
            if tmp[j + 1] - tmp[j] == tmp[j + 2] - tmp[j + 1]:
                if j == s - 3:
                    cnt += 1
            else:
                break

print(cnt)


