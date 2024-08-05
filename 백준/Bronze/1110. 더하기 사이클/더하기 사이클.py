def sol(x):
    if len(x) == 1:
        return str(int(x) * 11)
    res = x[-1]
    tmp = 0
    for i in x:
        tmp += int(i)
    res += str(tmp)[-1]
    return res


s = input()
now = sol(s)
cnt = 1
while 1:
    if int(now) == int(s):
        print(cnt)
        break
    now = sol(now)
    cnt += 1


