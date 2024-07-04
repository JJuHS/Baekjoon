from collections import deque as dq
n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right, now_sum, inf, res = 0, 0, arr[0], 1e10, 1e10

while 1:
    if now_sum < s:
        right += 1
        if right == n:break
        now_sum += arr[right]
    else:
        now_sum -= arr[left]
        res = min(res, right - left + 1)
        left += 1

print(int(res%inf))
