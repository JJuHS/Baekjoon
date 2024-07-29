a, res = input(), 0
for s in a:
    if s in 'ABC':res+=3
    elif s in 'DEF':res+=4
    elif s in 'GHI':res+=5
    elif s in 'JKL':res+=6
    elif s in 'MNO':res+=7
    elif s in 'PQRS':res+=8
    elif s in 'TUV':res+=9
    elif s in 'WXYZ':res+=10
print(res)