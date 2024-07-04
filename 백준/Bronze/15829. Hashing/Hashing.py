r = 31
M = 1234567891

alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# alphabet = {alphabet_list[i]:(i+1) for i in range(26)}

L = int(input())
string = input()
ans = 0

for i in range(L):
    ans += (1+alphabet_list.index(string[i]))*(r**i)
print(ans%M)