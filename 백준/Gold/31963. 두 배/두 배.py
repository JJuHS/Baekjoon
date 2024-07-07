n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n - 1):
    while True:
        if arr[i] > arr[i + 1]:
            arr[i + 1] *= 2
            cnt += 1
            continue
        break
print(cnt)