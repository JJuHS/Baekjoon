n=int(input())
res='*' * n
for i in range(n-1, 0, -1):
    res = '*'*i+'\n'+res+'\n'+'*'*i
print(res)