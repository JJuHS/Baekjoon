import math

def sol(x):
    tmp, res = [], 0
    for i in range(1, x):
        if x % i == 0:
            tmp.append(str(i))
            res+=i
    if res == x:print(f'{x} = {" + ".join(tmp)}');return
    else:print(f'{x} is NOT perfect.');return
while True:
    n = int(input())
    if n == -1:
        break
    sol(n)