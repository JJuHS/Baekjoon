n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(m)]
mid_x, mid_y = sorted(arr)[m // 2][0], sorted(arr, key=lambda x:x[1])[m // 2][1]
res = 0
for i in range(m):res += abs(mid_x - arr[i][0]) + abs(mid_y - arr[i][1])
print(res)