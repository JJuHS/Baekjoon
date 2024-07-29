import sys; input = sys.stdin.readline

l, n, k = map(int, input().split())
arr = list(map(int, input().split()))

if n >= k:
    print('0\n' * k)
    exit()

k -= n
print('0\n' * n, end='')
dist = 1

while True:
    dist_str = str(dist)
    for tmp in range(n):
        if (not tmp and arr[tmp] >= dist) or (tmp and arr[tmp] > arr[tmp - 1] + 2 * dist - 1):
            print(dist_str)
            k -= 1
        if not k:
            exit()
        if (tmp == n - 1 and arr[tmp] <= l - dist) or (tmp != n - 1 and arr[tmp] < arr[tmp + 1] - 2 * dist):
            print(dist_str)
            k -= 1
        if not k:
            exit()
    dist += 1

