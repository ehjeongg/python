#패키지를 이용하면 관련있는 모듈끼리 그룹화할 수 있음(package == directory)

#패키지 안에 있는 모듈을 사용할 때 import하는 방법
#from 패키지명(디렉토리명) import 모듈이름(파일명.py)

#site-package 모듈은 어디서나 쓸 수 있음(다른 디렉토리에 있는 모듈은 사용할 수 없음)

import sys
for path in sys.path :
    print(path) #모듈은 print해서 출력되는 모든 경로를 모두 찾음

#C:\Users\INSoft\AppData\Local\Programs\Python\Python311\Lib\site-packages 프로젝트 내에서 범용적으로 다 사용할 수 있는 곳

#원하는 모듈을 site-package로 옮기면 모든 디렉토리에서 접근가능함
#venv -> Lib -> site-packages 폴더로 옮기면 어느 디렉토리에서든지 원하는 모듈에 접근가능


#site_pac 패키지(폴더)를 site-packages로 옮겨서 다른 디렉토리 안에서도 사용할 수 있게 만들어음


#오류 발생된 부분
# from site_pac import divisor as d
#
# print(f'10의 약수 : {d.factor(10)}')
