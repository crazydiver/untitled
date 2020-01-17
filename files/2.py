with open('input.txt') as f:
    lst = f.readlines()
descr = {}
for i in lst:
    descr[int(i.split()[2])] = [descr.get(int(i.split()[3]), 0) + int(i.split()[3]), descr.get(int(i.split()[3]), 0) + 1]
print(descr)
