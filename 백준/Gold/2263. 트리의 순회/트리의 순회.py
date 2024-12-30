import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

tree = [0] * (n + 1)
for i in range(n):tree[inorder[i]] = i

def preorder(in_s, in_e, po_s, po_e):
    if in_s > in_e or po_s > po_e:return
    parent = postorder[po_e]
    print(parent, end = " ")

    left, right = tree[parent] - in_s, in_e - tree[parent]
    preorder(in_s, in_s + left - 1, po_s, po_s + left - 1)
    preorder(in_e - right + 1, in_e, po_e - right, po_e - 1)

preorder(0, n - 1, 0, n - 1)