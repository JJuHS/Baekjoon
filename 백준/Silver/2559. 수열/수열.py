n, k = map(int, input().split())
arr = list(map(int, input().split()))

p_sum = [-1e10] * n
p_sum[0] = sum(arr[:k])

for i in range(k, n):
    p_sum[i - k + 1] = p_sum[i - k] + arr[i] - arr[i - k]
print(max(p_sum))
