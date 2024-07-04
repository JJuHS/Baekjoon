N = int(input())

a = 1
b = []
i=1
while a<N:
    b.append(a)
    a += 6*i
    i+=1
print(len(b)+1)