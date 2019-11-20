n, m = map(int, input().split())
mas = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for i in range(n):
    count = 0
    for j in mas[i]:
        if j == 0:
            count += 1
        else:
            count = 0
        if count == k:
            print(i+1)
            exit()
print(0)
