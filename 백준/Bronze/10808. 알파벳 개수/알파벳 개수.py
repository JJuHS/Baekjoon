res=[0]*26
for s in input():
    res[ord(s)-97]+=1
print(*res)