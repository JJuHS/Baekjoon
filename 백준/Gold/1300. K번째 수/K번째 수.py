def main(n:int=int(input()), k:int=int(input())):
    s, e = 1, k
    while s <= e:
        mid = (s + e) // 2
        cnt = 0
        for i in range(1, n + 1):
            cnt += min(mid // i, n)

        if cnt >= k:
            res = mid
            e = mid - 1
        else:
            s = mid + 1
    print(res)

if __name__=='__main__':
    main()