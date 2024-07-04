a, b, c = input(), input(), input()
li = [a, b, c]
res = 0
for idx, num in enumerate(li):
    if num.isdigit():
        num = int(num)
        if idx == 0:
            res = num + 3
        if idx == 1:
            res = num + 2
        if idx == 2:
            res = num + 1
        break

if res % 3 == 0:
    if res % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif res % 5 == 0:
    print('Buzz')
else:
    print(res)