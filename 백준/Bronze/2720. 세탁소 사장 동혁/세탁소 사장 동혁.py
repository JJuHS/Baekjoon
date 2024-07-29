t = int(input())
for _ in range(t):
    m, res = int(input()), ''
    res += str(m // 25) + ' ';m %= 25
    res += str(m // 10) + ' ';m %= 10
    res += str(m // 5) + ' ';m %= 5
    res += str(m) + ' '
    print(res)
    