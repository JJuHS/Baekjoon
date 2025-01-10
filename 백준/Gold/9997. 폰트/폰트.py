import sys;input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
arr_bit = [0] * n

for i in range(n):
    char = arr[i]
    for s in char:
        arr_bit[i] |= 1 << (ord(s) - 97)

res = 0
goal = (1 << 26) - 1

def sol(now_bit=0, idx=0):
    global res
    if idx >= n:
        if now_bit == goal: 
            res += 1
        return
    
    sol(now_bit, idx + 1)
    sol(now_bit | arr_bit[idx], idx + 1)

sol()
print(res)