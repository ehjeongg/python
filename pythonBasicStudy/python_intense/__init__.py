# Calculator __init__() 호출
# Calculator() 생성자 호출
# cal = Calculator()

class Calculator:
    def __init__(self, n1, n2):
        print('[Calculator] __init__() called')
        self.num1 = n1
        self.num2 = n2


# cal = Calculator(10,20) #생성자 호출
# print(f'[cal.num1: {cal.num1}')
# print(f'[cal.num2: {cal.num2}')
#

#매개변수 없는 경우 / 개발자가 직접 임의의 수를 초기화한 경우 여러가지 테스트 해보기


