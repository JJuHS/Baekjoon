n = int(input())
arr = list(map(int, input().split()))
command = list(map(int, input().split()))
command = {
    '+': command[0],
    '-': command[1],
    '*': command[2],
    '/': command[3]
}
res_min, res_max = 1e10, -1e10

def sol(now=1, cnt=arr[0]):
    global res_max, res_min
    if now == n:
        res_max = max(res_max, cnt)
        res_min = min(res_min, cnt)
        return
    for i in ['+', '-', '*', '/']:
        if command[i]:
            command[i] -= 1
            if i == '+':
                sol(now+1, cnt + arr[now])
            elif i == '*':
                sol(now+1, cnt * arr[now])
            elif i == '-':
                sol(now+1, cnt - arr[now])
            elif i == '/':
                if cnt >= 0:
                    sol(now+1, cnt // arr[now])
                else:
                    sol(now+1, -(-cnt // arr[now]))
            command[i] += 1

sol()
print(res_max)
print(res_min)