import sys
input = sys.stdin.readline
n, t = map(int, input().split())
summation = [0] * 100002
end = 0
for i in range(n):
    k = int(input())
    for j in range(k):
        s, e = map(int, input().split())
        summation[s] -= 1
        summation[e] += 1
        end = max(end, e)

tmp = 0
for i in range(t):
    summation[i + 1] += summation[i]
    tmp += summation[i]

res = tmp
s, e = 0, t
for i in range(t, end + 1):
    summation[i + 1] += summation[i]
    tmp += summation[i] - summation[i - t]
    if tmp < res:
        s, e, tmp = i - t + 1, i + 1, res

print(s, e)
