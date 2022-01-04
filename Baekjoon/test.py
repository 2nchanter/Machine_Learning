import sys
a = int(sys.stdin.readline().strip())
n = 0
b = (a//10)+(a%10)
c = (a%10*10)+(b%10)
print(c)