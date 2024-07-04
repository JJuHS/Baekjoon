import sys
N = int(input())
b = []
for n in range(N):
    a = int(sys.stdin.readline())
    b.append(a)

print(round(sum(b)/N))
print(sorted(b)[N//2])
count = [0]*8001
for i in b:
    count[i+4000] += 1

m = []
for j in range(len(count)):
    if count[j] == max(count):
        m.append(j-4000)
if len(m)==1:
    print(m[0])
else:
    m.sort()
    print(m[1])


print(max(b)-min(b))