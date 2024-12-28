import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from collections import defaultdict

n = int(input())    # 배열 길이
A = ''
for num in map(int, input().split()):
    A += str(num -1) # 배열 A를 str로 받기
goal = ''.join(sorted(A))

m = int(input())    
commands = [list(map(int, input().split())) for _ in range(m)] # 명령어 배열

costs = defaultdict()
costs[A] = 0

q = [(0, A)]    # 비용, 현재 문자열

while q:
    cost, now = heappop(q)
    if costs[now] > cost:continue   # 최솟값보다 커지면 안 함
    if now == goal:continue
    for l, r, c in commands:
        next_str = now[:l-1] + now[r-1] + now[l:r-1] + now[l-1] + now[r:]
        if next_str in costs and costs[next_str] <= cost + c:continue
        costs[next_str] = cost + c
        heappush(q, (cost + c, next_str))

print(costs[goal] if goal in costs else -1)
