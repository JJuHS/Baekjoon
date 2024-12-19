import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)

for _ in range(m):
    pd_arr = list(map(int, input().split()))
    for singer in range(1, pd_arr[0]):
        arr[pd_arr[singer]].append(pd_arr[singer + 1])
        visit[pd_arr[singer + 1]] += 1

un_nominated = []
for i in range(1, n + 1):
    if visit[i] == 0: un_nominated.append(i)

res = []

while un_nominated:
    now = un_nominated.pop()
    res.append(str(now))

    for i in arr[now]:
        visit[i] -= 1
        if visit[i] == 0:un_nominated.append(i)

if len(res) == n:
    print('\n'.join(res))
else:
    print(0)

