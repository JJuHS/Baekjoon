import sys; input=sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
numbers = [0 for _ in range(1000001)]
for num in arr:
    numbers[num] = 1
res = [0 for _ in range(1000001)]

max_number = max(arr) + 1
for num in arr:
    for check in range(num * 2, max_number, num):
        if numbers[check]:
            res[num] += 1
            res[check] -= 1

for num in arr:
    print(res[num], end=' ')
