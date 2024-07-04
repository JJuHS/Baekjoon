K = int(input())
result = []
for k in range(K):
    num_ = int(input())
    if num_ != 0:
        result.append(num_)
    else:
        result.pop()
print(sum(result))