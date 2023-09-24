n = int(input())

for star in range(1, n):
    print(' ' * (n - star), end='')
    print(star * ' *')
for s in range(n, 0, -1):
    print(' ' * (n - s), end='')
    print(s * ' *')
