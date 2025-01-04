import sys
input = sys.stdin.readline

for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    n, arr = tmp[0], tmp[1:]
    avg = sum(arr) / n
    res = 100 * sum([1 for i in range(n) if arr[i] > avg]) / n
    print(f'{res:.3f}%')
