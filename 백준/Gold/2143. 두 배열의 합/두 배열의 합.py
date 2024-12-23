import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline

from collections import defaultdict

t = int(input())

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# 부분집합의 합 구해놓기, 단 인덱스가 연속이어야 함
def subset_sum(N, arr):
    dict_arr = defaultdict(int)
    # 크기가 x 인 부분집합
    for x in range(1, N + 1):
        # 누적합 알고리즘
        s = sum(arr[:x])
        dict_arr[s] += 1
        for i in range(1, N - x + 1):
            s += arr[i + x - 1] - arr[i - 1]
            dict_arr[s] += 1 

    return dict_arr

dict_A = subset_sum(n, a)
dict_B = subset_sum(m, b)

res = 0

for k_A, v_A in dict_A.items():
    res += v_A * dict_B[t - k_A]

print(res)