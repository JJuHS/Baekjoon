import sys; input = sys.stdin.readline
n, q = map(int, input().split())
votes = [0] * (n + 2)
for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        votes[c] += b
    if a == 2:
        my_vote = votes[-1] + b
        res = 0
        for vote in votes[1:n+1]:
            if my_vote > vote + c:
                res = 1
                break
        print(['NO', 'YES'][res])

