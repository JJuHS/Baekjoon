import sys
input = sys.stdin.readline


def friend(x, y):
    set_y = set(y)
    for idx, num in enumerate(x[:-1]):
        x[idx] += 1
        x[idx + 1] -= 1
        if set(x) == set_y:
            return True
        x[idx] -= 1
        x[idx + 1] += 1
        if idx != 0 or num != 1:
            x[idx] -= 1
            x[idx + 1] += 1
            if set(x) == set_y:
                return True
            x[idx] += 1
            x[idx + 1] -= 1
    return False


for _ in range(3):
    X, Y = map(list, input().split())
    for i in range(len(X)):
        X[i] = int(X[i])
    for i in range(len(Y)):
        Y[i] = int(Y[i])

    if set(X) == set(Y):
        print('friends')
        continue
    if friend(X, Y) or friend(Y, X):
        print('almost friends')
    else:
        print('nothing')
