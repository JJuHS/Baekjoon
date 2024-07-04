a, k = map(int, input().split())
cnt = 0
while not a == k:
    cnt += 1
    if k % 2 == 0 and k//2 >= a:
        k //= 2
        continue
    k -= 1
print(cnt)