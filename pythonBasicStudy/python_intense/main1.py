#__name__에는 모듈 이름 또는 __main__이 저장된다
#실행파일은 __main__을 찾아간다(java에서의 main methods같은 것 - 어떤 것을 먼저 시작할 지 정하는 것)

import add
import mul

#다른 파일에서 main1 파일의 mod함수만 쓰고 싶을때, 이미 해당파일에 import되어있는 add, mul은 필요없으니 12번 라인처럼 작성
def mod(x,y):
    return x % y


if __name__ == '__main__':  # 실행파일 == 메인이라면 아래를 출력
    print(add.addCal(1, 2))
    print(mul.mulCal(2, 3))












