import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [int(input()) for _ in range(n)]

# 세그먼트 트리 만들어주기
seg = [0 for _ in range(4 * n)]

def make_tree(l:int=0, r:int=(n-1), x:int=1):
    if l == r:
        seg[x] = graph[l]
        return seg[x]
    mid = (l + r) // 2
    seg[x] = make_tree(l, mid, 2*x) + make_tree(mid + 1, r, 2*x + 1)
    return seg[x]

make_tree()

def find_tree(l:int, r:int, x:int, b:int, c:int):
    if c < l or r < b:return 0  # 구간 밖
    if b <= l and r <= c:return seg[x]  # 구간 < 현재 트리
    mid = (l + r) // 2
    return find_tree(l, mid, x*2, b, c) + find_tree(mid + 1, r, x*2 + 1, b, c)

# seg[idx]를 v로 바꾸기
def modify_tree(l:int, r:int, x:int, idx, v):
    if l == r == idx:
        seg[x] = v
        return
    if l > idx or r < idx:return
    mid = (l + r) // 2
    modify_tree(l, mid, x*2, idx, v)
    modify_tree(mid + 1, r, x*2 + 1, idx, v)

    seg[x] = seg[x*2] + seg[x*2 + 1]

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        modify_tree(0, n-1, 1, b-1, c)   # 숫자 변경
    else:
        print(find_tree(0, n - 1, 1, b - 1, c - 1))  # 누적합 출력