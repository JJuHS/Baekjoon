import sys;input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    s = input()
    if s[0] == '1':stack.append(int(s[2:]))
    if s[0] == '2':print(stack.pop() if stack else -1)
    if s[0] == '3':print(len(stack))
    if s[0] == '4':print(0 if stack else 1)
    if s[0] == '5':print(stack[-1] if stack else -1)