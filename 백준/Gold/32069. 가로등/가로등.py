import sys;input = sys.stdin.readline

l, n, k = map(int, input().split()) # 도로 길이, 가로등 개수, 출력개수
arr = list(map(int, input().split()) ) # 가로등 배열

visit = []
res = ''
total = 0
idx = 0
while True:
    if total == k:
        break
    for i in arr:
        if i + idx <= l and (i + idx) not in visit:
            visit.append(i + idx)
            res += str(idx) + '\n'
            total += 1
        if total == k:
            break
        if i - idx >= 0 and (i - idx) not in visit:
            visit.append(i - idx)
            res += str(idx) + '\n'
            total += 1
        if total == k:
            break
    idx += 1
    
print(res)