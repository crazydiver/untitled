import string

print(sum([i.strip(string.punctuation).isalpha() for i in input().split()]))
