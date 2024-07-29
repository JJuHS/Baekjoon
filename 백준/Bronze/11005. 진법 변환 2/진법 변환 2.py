n, b = map(int, input().split())
res = ''
while n:
    if n % b >= 10:res = chr(n % b + 55) + res
    else:res = str(n % b) + res
    n //= b
print(res)