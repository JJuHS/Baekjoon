import sys
input = sys.stdin.readline


def binary(s, e, li, goal):
    while s <= e:
        m = (s + e) // 2
        if li[m] >= goal:
            e = m - 1
        else:
            s = m + 1
    return s


n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()

dp = [-1] * n
ans = [arr[0][1]]
for i in range(n):
    if ans[-1] < arr[i][1]:
        dp[i] = max(dp) + 1
        ans.append(arr[i][1])
    else:
        tmp = binary(0, len(ans) - 1, ans, arr[i][1])
        if arr[i][1] > ans[tmp]:
            ans[-1] = arr[i][1]
        else:
            ans[tmp] = arr[i][1]
            dp[i] = tmp + 1
print(n - len(ans))


now = len(ans)
tmp = []

for i in range(n - 1, -1, -1):
    if now == 0:
        break
    if dp[i] == now:
        tmp.append(arr[i])
        now -= 1

res = []
for i in arr:
    if i not in tmp:
        res.append(i)
res.sort()

for i in range(n - len(ans)):
    print(res[i][0])