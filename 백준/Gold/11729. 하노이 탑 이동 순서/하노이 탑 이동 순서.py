ans = {}
def hanoi(x, board1, board3, board2):
    key = (x, board1, board3, board2)
    if key in ans:
        return ans[key]
    if x == 1:
        return f'{board1} {board3}'
    tmp = '\n'.join([hanoi(x - 1, board1, board2, board3), f'{board1} {board3}', hanoi(x - 1, board2, board3, board1)])
    ans[key] = tmp
    return tmp

n = int(input())
res = hanoi(n, '1', '3', '2')

print(2 ** n - 1)
print(res)