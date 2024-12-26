import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline
import math
a, b = map(int, input().split())

def sol(x):
    if x <= 0:return 0
    index = int(math.log2(x))
    max_exponential = 1 << index # x 보다 작은 수 중 제일 큰 2**n
    if max_exponential == x:
        return index * x // 2 + 1
    return sol(x - max_exponential) + x - max_exponential + sol(max_exponential)

print(sol(b) - sol(a-1))