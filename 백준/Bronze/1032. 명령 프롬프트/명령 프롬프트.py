
n=int(input())
s=input()
arr=[1]*len(s)
if n>1:
    for _ in range(n-1):
        c=input()
        for i in range(len(s)):
            if c[i]!=s[i]:
                arr[i]=0
res = [s[i] if arr[i]==1 else '?' for i in range(len(s))]
print(''.join(res))