n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
ans = -1


def ms(p, r):
    if p < r:
        if res <= k:
            mid = (p + r) // 2
            ms(p, mid)
            ms(mid + 1, r)
            m(p, mid, r)


def m(p, q, r):
    global res, ans
    i, j, t, tmp = p, q + 1, -1, []
    while i <= q and j <= r:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= q:
        tmp.append(arr[i])
        i += 1
    while j <= r:
        tmp.append(arr[j])
        j += 1
    i, t = p, 0
    while i <= r:
        arr[i] = tmp[t]
        res += 1
        if res == k:
            ans = arr[i]
            break
        i += 1
        t += 1

ms(0, n - 1)
print(ans)