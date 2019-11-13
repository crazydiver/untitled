s = input()
print([isinstance(i, str) for i in s.split()].count(True))
