import sys

ans = 0
for i in range(10):
    score = int(sys.stdin.readline())
    ans_tmp = ans
    ans += score
    if ans >= 100:
        if ans - 100 > 100 - ans_tmp:
            ans = ans_tmp
        break
print(ans)