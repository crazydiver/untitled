s = input().lower()
ns = 0
i = 0
while not s[i].isalpha():
    s = s[i + 1:]
    i += 1
i = len(s) - 1
while not s[i].isalpha():
    s = s[: i]
    i -= 1
for i, j in enumerate(s):
    if j.isalpha() and not s[i-1].isalpha():
        ns += 1
print(ns + 1)
# ..,/,./ecwvre ,./bweb ,/.
