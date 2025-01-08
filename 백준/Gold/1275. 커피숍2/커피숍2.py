import sys;input = sys.stdin.readline

def make_seg(n, arr):
    seg = [0] * (4 * n)
    def make(node, s, e):
        if s == e:
            seg[node] = arr[s]
            return seg[node]
        mid = (s + e) // 2
        seg[node] = make(node * 2 + 1, s, mid) + make(node * 2 + 2, mid + 1, e)
        return seg[node]
    make(0, 0, n - 1)
    return seg

def find_seg(seg, x, y, node, s, e):
    if x > e or y < s: return 0
    if x <= s and e <= y: return seg[node]
    mid = (s + e) // 2
    return find_seg(seg, x, y, node * 2 + 1, s, mid) + find_seg(seg, x, y, node * 2 + 2, mid + 1, e)

def update_seg(seg, idx, num, node, s, e):
    if s== e:seg[node] = num;return
    mid = (s + e) // 2
    if s <= idx <= mid:
        update_seg(seg, idx, num, node * 2 + 1, s, mid)
    else:
        update_seg(seg, idx, num, node * 2 + 2, mid + 1, e)
    seg[node] = seg[node * 2 + 1] + seg[node * 2 + 2]


if __name__ == '__main__':
    N, Q = map(int, input().split())
    Arr = list(map(int, input().split()))
    seg = make_seg(N, Arr)

    for _ in range(Q):
        X, Y, A, B = map(int, input().split())
        print(find_seg(seg, min(X, Y) - 1, max(X, Y) - 1, 0, 0, N - 1))
        update_seg(seg, A - 1, B, 0, 0, N - 1)
