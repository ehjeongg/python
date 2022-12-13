#module은 import / from / as 를 통해서 사용한다.

import module_user as mo
#긴 모듈명 대신에 as ~ 로 써서 모듈을 더 간단하게 사용할 수 있다.

mo.add(10,20)

num = mo.getLotto()
print(num)

userInput = input('문자입력')
reverse = mo.rever(userInput)
print(reverse)

#from ~ import ~ 키워드를 통해서 모듈의 '특정한 기능'만 사용가능
from module_user import sub
sub(30,10) #이 경우 모듈명을 쓰지 않고 함수명만 바로쓴다.

#from module_user import *  : 해당 모듈에 있는 전 기능을 사용하겠다는 의미
#from module_user import getLotto, add, sub, mul : 원하는 기능을 ,로 여러개 불러올 수 있음

