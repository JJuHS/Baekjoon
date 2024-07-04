import sys

n = int(input())
time_money = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(n):
        if time_money[i] > time_money[j]:
            time_money[i],time_money[j] = time_money[j], time_money[i]

time_need = [(i+1) * time_money[i] for i in range(n)]

print(sum(time_need))