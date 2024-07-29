while True:
    a, b, c = map(int, input().split())
    if a == 0:break
    if a + b <= c or b + c < a or a + c < b:print('Invalid');continue
    if a == b == c:print('Equilateral');continue
    if a == b or b == c or a == c:print('Isosceles');continue
    print('Scalene')