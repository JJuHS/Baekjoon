res = [0] * 10
for n in input():
    n=int(n)
    if n == 9:res[6]+=1
    else:res[n]+=1
res[6] = res[6] // 2 + res[6]%2
print(max(res))