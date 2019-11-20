n = int(input())
dic = (i for i in range(n))
while True:
    ip = input()
    if ip == 'HELP':
        break
    if ip not in ('YES', 'NO', 'HELP'):
        mlp = set(map(int, input().split()))
    if ip == 'YES':
        dic = dic & mlp
    if ip == 'NO':
        dic = dic - mlp
print(*dic)
