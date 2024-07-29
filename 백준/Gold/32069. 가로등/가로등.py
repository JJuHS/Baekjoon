import sys
input = sys.stdin.readline

l, n, k = map(int, input().split())
arr = list(map(int, input().split()))
if n >= k:
    print('0\n' * k)
    exit()
visit = []
res = ''
distance = 0
flag = True
while flag:
    for now in arr:
        if now + distance <= l and (now + distance) not in visit:
            visit.append(now + distance)
            res += str(distance) + '\n'
            k -= 1
            if k == 0:
                flag = False
                break
        if now - distance >= 0 and (now - distance) not in visit:
            visit.append(now - distance)
            res += str(distance) + '\n'
            k -= 1
            if k == 0:
                flag = False
                break

    distance += 1
print(res)