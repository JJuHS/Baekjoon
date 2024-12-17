import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline
sys.setrecursionlimit(100000)

v, e = map(int, input().split())
arr = []

for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

arr.sort(key=lambda x: x[2])

sum_weight = 0
parents = [i for i in range(v + 1)]

def union(x):
    if parents[x] == x: return x
    parents[x] = union(parents[x])
    return parents[x]

def union_set(x, y):
    x, y = union(x), union(y)
    if x == y:return
    if x < y: parents[y] = x
    if x > y: parents[x] = y

for a, b, c in arr:
    if union(a) == union(b):continue
    union_set(a, b)
    sum_weight += c

print(sum_weight)