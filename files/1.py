s = input().lower()
ns = 0
for i in s:
    if i not in 'qwertyuiopasdfghjklzxcvbnm,.1234567890':
        ns += 1
print(ns + 1)
