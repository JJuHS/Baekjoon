n, k = map(int, input().split())
print(sum(sorted(list(map(int, input().split())), reverse=True)[:k]) - k*(k-1)//2)