import sys;input=sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

res = [-1] * n
stack = [0]

for i in range(1, n):
    while stack:
        if arr[stack[-1]] >= arr[i]:
            break
        res[stack.pop()] = arr[i]
    stack.append(i)

print(*res)
    