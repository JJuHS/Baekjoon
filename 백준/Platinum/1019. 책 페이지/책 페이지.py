import sys
input = sys.stdin.readline
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

def sol(n: str):
    res = [0] * 10  
    n = int(n)

    factor = 1 

    while n >= factor:
        current = (n // factor) % 10  # 현재 자리 숫자
        higher = n // (factor * 10)  # 더 높은 자리 숫자
        lower = n % factor  # 더 낮은 자리 숫자

        for i in range(10):
            if i < current:
                res[i] += (higher + 1) * factor
            elif i == current:
                res[i] += higher * factor + (lower + 1)
            else:
                res[i] += higher * factor

        res[0] -= factor

        factor *= 10

    print(*res)

sol(input())
