import sys
input = sys.stdin.readline
s, d = list(input().rstrip()), list(input().rstrip())
n = len(d)

stack = []
for w in s:
    stack.append(w)
    if stack[-1] == d[-1]:
        if len(stack) >= n:
            if stack[-n:] == d:
                for i in range(n):
                    stack.pop()
print(''.join(stack) if stack else 'FRULA')