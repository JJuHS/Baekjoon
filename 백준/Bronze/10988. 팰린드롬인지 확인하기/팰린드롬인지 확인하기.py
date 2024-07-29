s = input()
for i in range(len(s)//2):
    if s[i] == s[-i-1]:continue
    print(0);exit(0)
print(1)