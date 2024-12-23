import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, r, q = map(int, input().split()) # 2 ≤ N ≤ 10^5, 1 ≤ R ≤ N, 1 ≤ Q ≤ 10^5

res = [0] * (n + 1)
tree = [[] for _ in range(n + 1)]

# 루트있는 트리
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 서브트리 만들기
def dfs(x):
    res[x] = 1
    for i in tree[x]:
        if not res[i]:
            dfs(i)
            res[x] += res[i]
dfs(r)

# u를 루트로 하는 서브트리의 정점 수 출력
for _ in range(q):
    u = int(input())
    print(res[u])
