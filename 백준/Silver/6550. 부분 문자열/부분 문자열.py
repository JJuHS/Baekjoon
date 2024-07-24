def sol(x, y):
    for char in y:
        if x and char == x[0]:
            x.pop(0)
    if x:return 0
    return 1


while True:
    try:
        s, t = map(str, input().split())
        s = list(s)
        print(['No', 'Yes'][sol(s, t)])
    except:break