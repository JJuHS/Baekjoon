import math
import sys; input = sys.stdin.readline


def sol(arr, n):
    tmp = 0
    cnt_arr = [0] * n
    for i in range(1, n):
        tmp_cnt = math.ceil(math.log2(arr[i - 1] / arr[i])) + cnt_arr[i - 1]
        if tmp_cnt > 0:
            cnt_arr[i] = max(0, math.ceil(math.log2(arr[i - 1] / arr[i])) + cnt_arr[i - 1])
            tmp += cnt_arr[i]
    return tmp


n = int(input())
arr = list(map(int, input().split()))

print(sol(arr, n))
