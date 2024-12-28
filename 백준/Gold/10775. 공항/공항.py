import sys

# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")
input = sys.stdin.readline

g, p = int(input()), int(input())

planes = [int(input()) for _ in range(p)]
gates = [i for i in range(g + 1)]

def sol(plane):
    if gates[plane] == plane:
        return plane
    gates[plane] = sol(gates[plane])
    return gates[plane]

res = 0
for i, plane in enumerate(planes):
    docked = sol(plane)
    if not docked:break
    gates[docked] = gates[docked - 1]
    res += 1
print(res)