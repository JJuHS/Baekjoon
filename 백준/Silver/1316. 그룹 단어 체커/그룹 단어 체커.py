n, res = int(input()), 0
for _ in range(n):
    s = input()
    now, flag = s[0], True
    ar = [now]
    for i in range(len(s)):
        if not flag:break
        if s[i] == now:continue
        if s[i] in ar:flag=False;break
        ar.append(s[i])
        now=s[i]
    if flag:res+=1
print(res)