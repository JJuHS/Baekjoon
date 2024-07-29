arr = [list(map(int, input().split())) for _ in range(3)]
a = [arr[i][0] for i in range(3)]
b = [arr[i][1] for i in range(3)]
print(2 * sum(set(a)) - sum(a), 2 * sum(set(b)) - sum(b))
