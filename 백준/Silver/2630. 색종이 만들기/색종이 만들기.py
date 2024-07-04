import sys

N = int(input())

confetti = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = []

def color(li, n, s = 0, e = 0):
    tmp = confetti[s][e]
    for i in range(s, s + n):
        for j in range(e, e + n):
            if confetti[i][j] != tmp:
                color(li, n//2, s, e)
                color(li, n//2, s, e + n//2)
                color(li, n//2, s + n//2, e)
                color(li, n//2, s + n//2, e + n//2)
                return
    ans.append(tmp)

color(confetti, N)
print(ans.count(0))
print(ans.count(1))







