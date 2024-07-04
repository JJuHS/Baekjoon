import sys
n, m = map(int, sys.stdin.readline().split())

live_dict = {}
certainly_ = []
never = []

for i in range(m):
    str_tmp = ''.join(sys.stdin.readline().split())
    live_dict[str_tmp[:-1]] = str_tmp[-1]
    
for k, v in live_dict.items():
    a, b, c = k[:-1], k[-1], v

    if b == 'P':
        if c == '1':
            certainly_.append(a)
        else:
            never.append(a)
    else:
        if c == '0':
            certainly_.append(a)
        else:
            never.append(a)

certain = 0

for live_thing in set(certainly_):
    if certainly_.count(live_thing) == 2:
        certain += 1

max_ = n - len(set(never))

print(certain, max_)