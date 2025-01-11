arr = [int(input()) for _ in range(9)]
now = sum(arr)
for i in range(8):
    for j in range(i + 1, 9):
        if now - arr[i] - arr[j] == 100:
            arr.pop(i)
            arr.pop(j-1)
            print('\n'.join([str(i) for i in sorted(arr)]))
            exit()