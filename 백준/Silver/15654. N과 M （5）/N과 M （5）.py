n, m = map(int, input().split())
from itertools import permutations
for arr in permutations(sorted(list(map(int, input().split()))), m):
    print(*arr)