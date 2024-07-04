a = [a for a in range(1,31)]
b = []
for i in range(28):
    c = int(input())
    b.append(c)
d = list(set(a).difference(b))
d.sort()
print(d[0],d[1])