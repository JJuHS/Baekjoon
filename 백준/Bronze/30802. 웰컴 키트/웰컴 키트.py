n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())
res1 = 0
for i in arr: res1 += i//t + bool(i%t)
print(res1)
print(sum(arr)//p , sum(arr)%p)
