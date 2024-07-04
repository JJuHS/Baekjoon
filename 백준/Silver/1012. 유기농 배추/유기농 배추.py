import sys
sys.setrecursionlimit(50000)

def find_num(a,b):
    x = [1,0,-1,0]
    y = [0,1,0,-1]
    land[a][b] = 0
    for i in range(4):
        aa = a + x[i]
        bb = b + y[i]
        if (aa >= n) or (bb >= m) or (aa < 0) or (bb < 0):
            continue
        if land[aa][bb] == 1:
            find_num(aa,bb)

T = int(input())
for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    land = [[0]*m for __ in range(n)]
    
    for _ in range(k):
        land1, land2 = map(int, sys.stdin.readline().split())
        land[land2][land1] = 1

    worms_count = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                worms_count += 1
                find_num(i,j)

    print(worms_count)