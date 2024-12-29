# 숭실대 지도 그리기
arr = [[0] * 8 for _ in range(8)]
arr[0][1], arr[1][0] = 1, 1
arr[0][2], arr[2][0] = 1, 1
arr[1][2], arr[2][1] = 1, 1
arr[1][3], arr[3][1] = 1, 1
arr[2][3], arr[3][2] = 1, 1
arr[2][4], arr[4][2] = 1, 1
arr[3][4], arr[4][3] = 1, 1
arr[3][5], arr[5][3] = 1, 1
arr[4][5], arr[5][4] = 1, 1
arr[4][7], arr[7][4] = 1, 1
arr[5][6], arr[6][5] = 1, 1
arr[6][7], arr[7][6] = 1, 1
div = 1000000007

# 경로 찾기
def sol(d, grp = arr):
    if d == 1:
        return grp
    grp_n = sol(d // 2, grp)
    if not d % 2:
        return multiple(grp_n, grp_n)
    else:
        return multiple(multiple(grp_n, grp_n), grp)

# 행렬 곱
def multiple(x, y):
    res = [[0]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for m in range(8):
                res[i][j] += x[i][m] * y[m][j]
            res[i][j] %= div
    return res
        
ans = sol(int(input()))
print(ans[0][0])
