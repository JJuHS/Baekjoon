
def dfs(Node,level):

    visit[Node]=True
    if Node==P:
        visit[P]=False
        if len(length)<=1:
            length.append(level)
        else:
            if level < max(length):
                del length[length.index(max(length))]
                length.append(level)
        return
    for i in Tree[Node]:
        if not visit[i]:
            dfs(i,level+1)
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

N,S,P=map(int,input().split())
Tree=[ [] for _ in range(N+1) ]

for i in range(N-1):
    A,B=map(int,input().split())
    Tree[A].append(B)
    Tree[B].append(A)

visit=[False]*(N+1)
length=[]

for i in range(1,S+1):
    if not visit[i] and i!=P:
        dfs(i,0)

print(N-sum(length)-1)