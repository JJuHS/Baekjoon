import sys
n = int(input())
coordinate = list(map(int, sys.stdin.readline().split()))
coordinate2 = sorted(list(set(coordinate)))
ans_dict = {}

for i in range(len(coordinate2)):
    ans_dict[coordinate2[i]] = i

for i in coordinate:
    print(ans_dict[i], end = ' ')
