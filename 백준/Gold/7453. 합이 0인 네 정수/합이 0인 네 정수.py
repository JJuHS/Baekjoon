import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = [a + b for a in A for b in B]  # 16,000,000
CD = [-(c + d) for c in C for d in D]  # 16,000,000

AB.sort()
CD.sort()
res = 0

i, j = 0, 0

while i < len(AB) and j < len(CD):
    if AB[i] == CD[j]:
        i_tmp, j_tmp = i, j
        value = AB[i]

        while i < len(AB) and AB[i] == value:
            i += 1
        while j < len(CD) and CD[j] == value:
            j += 1
        
        res += (i - i_tmp) * (j - j_tmp)

    elif AB[i] > CD[j]:
        j += 1
    else:
        i += 1

print(res)