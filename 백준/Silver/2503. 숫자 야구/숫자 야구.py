arr = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i==j or j==k or k==i: continue
            arr.append(str(100*i+10*j+k))

n = int(input())

no_ans = []
for _ in range(n):
    tmp, s, b = map(int, input().split())
    tmp = str(tmp)
    for i in range(len(arr)):
        if arr[i] in no_ans: continue
        num_s, num_b = 0, 0
        for j in range(3):
            if tmp[j] in arr[i]:
                if arr[i][j] == tmp[j]: num_s += 1
                else: num_b += 1
        if s != num_s or b != num_b: no_ans.append(arr[i])

print(len(arr) - len(no_ans))