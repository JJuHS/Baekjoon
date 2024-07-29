x, i = int(input()), 1
while x > 0:x, i = x - i, i + 1
print([f'{1 - x}/{x + i - 1}', f'{x + i - 1}/{1 - x}'][i%2])