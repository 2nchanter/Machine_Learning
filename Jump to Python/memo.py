import sys

option = sys.argv[1] # arguments vector, 가변적인 개수의 문자열. 프로그램을 실행할 때 입력된 값을 읽어 들일 수 있는 파이썬 라이브러리.

if option == "-a":
    memo = sys.argv[2]
    with open('memo.txt', 'a') as f:
        f.write(memo)
        f.write('\n')
elif option == "-v":
    with open('memo.txt') as f:
        memo = f.read()
        print(memo)