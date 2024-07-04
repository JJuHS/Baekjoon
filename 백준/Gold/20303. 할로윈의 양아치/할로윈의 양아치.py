import sys
input = sys.stdin.readline

def union_find(x):
    if parent[x] != x:
        return union_find(parent[x])
    return x


def union_set(x, y):
    x = union_find(x)
    y = union_find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def rob(s):
    for j in range(k - 1, friends_num[s] - 1, -1):
        dp[j] = max(dp[j], dp[j - friends_num[s]] + candies[s])
    return


n, m, k = map(int, input().split())
candies = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union_set(a, b)

friends_num = [1] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if parent[i] != i:
        candies[union_find(i)] += candies[i]
        friends_num[union_find(i)] += friends_num[i]

for i in range(1, n + 1):
    if i == parent[i]:
        rob(i)

print(max(dp))