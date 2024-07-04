import sys
from bisect import bisect_right as br

# 입력 받기
n, m, k = map(int, input().split())
pushed_h20 = sorted(list(map(int, input().split())))  # 민수가 가진 파란색 카드의 번호
fe_h20 = list(map(int, input().split()))  # 철수가 순서대로 낼 카드의 번호
arr = list(range(m))

# union-find 알고리즘을 이용하여 카드 집합 관리
def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]

# # 두 카드의 집합을 합치는 함수
# def union(x, y):
#     if y >= m:  # 철수가 더 이상 카드를 내지 않을 때
#         return
#     x = find(x)
#     y = find(y)
#     arr[x] = y

# 철수가 카드를 낼 때마다 민수가 낼 카드를 결정하고 출력
for i in fe_h20:
    idx = br(pushed_h20, i)  # 이진 탐색을 통해 철수가 내는 카드의 위치를 찾음
    idx = find(idx)  # 현재 카드의 집합을 확인
    print(pushed_h20[idx])  # 민수가 낼 카드 출력
    arr[idx] += 1  # 철수가 내는 카드가 더이상 사용되지 않도록 카운트 증가
