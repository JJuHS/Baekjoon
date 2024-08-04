import math
def sol(x):
    if x == 0:return ['*']
    tmp = sol(x - 1)
    res1, res2, res3 = [], [], []
    for i in tmp:
        res1.append(i * 3)
        res2.append(i + ' '*3**(x - 1) + i)
        res3.append(i * 3)
    return res1 + res2 + res3

print('\n'.join(sol(int(round(math.log(int(input()), 3))))))
