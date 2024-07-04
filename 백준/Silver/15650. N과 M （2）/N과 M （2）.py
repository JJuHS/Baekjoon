n, m = map(int, input().split())
from itertools import combinations
for arr in combinations(range(1, n + 1), m):
    print(*arr)