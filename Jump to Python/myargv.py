import sys
a = sys.argv[1:]
A = 0
for i in a:
    A += int(i)
print(A)
# print(sum(list(sys.argv)))