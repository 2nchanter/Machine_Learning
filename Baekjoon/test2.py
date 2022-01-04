import sys
A = sys.stdin.readline().strip()
a = int(A)
n = 0
while True:
    n += 1
    b = (a//10)+(a%10)
    c = (a%10*10)+(b%10)
    if int(A) == c:
        print(n)
        break
    a = c