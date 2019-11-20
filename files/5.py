n, m = map(int, input().split())
a = [[1] * m] * n
for i in range(m):
    print('{:6d}'.format(1), end='')
print()
for i in range(1, n):
    print('{:6d}'.format(1), end='')
    for j in range(1, m):
        a[i][j] = a[i-1][j] + a[i][j-1]
        print('{:6d}'.format(a[i][j]), end='')
    print()
