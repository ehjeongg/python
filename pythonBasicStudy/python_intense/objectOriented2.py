#게산기 클래스를 만들어 사칙연산 해보기

class Calculator:
    def __init__(self): #매개변수없이 클래스가 만들어진 경우 객체 생성시에도 매개변수 없이 생성자만 호출
        self.number1= 0
        self.number2 =0
        self.result = 0

    def add(self):
        self.result = self.number1+self.number2
        return self.result

    def sub(self):
        self.result = self.number1 - self.number2
        return self.result

    def mul(self):
        self.result = self.number1 * self.number2
        return self.result

    def div(self):
        self.result = self.number1 / self.number2
        return self.result

#매개변수없이 클래스가 만들어진 경우 객체 생성시에도 매개변수 없이 생성자만 호출 (객체를 담을 변수 = 생성자(클래스이름(매개변수 속성값등``)

# 생성된 객체를 담을 변수 = 클래스명()
cal = Calculator() #매개변수 속성값 없이 호출된 모습

print('cal = Calculator() => 중요한것은 클래스를 통해서 생성자를 만들어야하는것')
print()
print('직접 속성값을 할당하고 0에서 임의 값으로 변경 한 것')
cal.number1 = 5
cal.number2 = 7

print(f'곱셈결과 : {cal.mul()}')
print(f'덧셈결과 : {cal.add()}')

print()

print('입력 값을 받은 것')
userInt1 = int(input('숫자1 입력:'))
userInt2 = int(input('숫자2 입력:'))

cal.number1 = userInt1
cal.number2 = userInt2

print()

print(f'곱셈결과 : {cal.mul()}')
print(f'덧셈결과 : {cal.add()}')