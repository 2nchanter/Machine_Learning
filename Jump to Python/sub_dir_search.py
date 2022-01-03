import os

def search(dirname):
    try:
        filesname = os.listdir(dirname) # 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다.
        for filename in filesname:
            full_filename = os.path.join(dirname, filename) # 인수에 전달된 2개의 문자열을 결합하여, 1개의 경로로 할 수 있다.
            if os.path.isdir(full_filename):
                search(full_filename) # 재귀호출
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError: # os.listdir를 수행할 때 권한이 없는 디렉터리에 접근하더라도 프로그램이 오류로 종료되지 않고 그냥 수행되도록 하기 위해
        pass   

search("/Users/young/Shioame27/0_Coding/Machine_Learning/Jump to Python")