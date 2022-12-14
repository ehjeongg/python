class Cal1: #부모클래스
    def __init__(self): # 매개변수를 넣어줄 경우 더 간단하게도 표현할 수 있음
        self.n1 = 0
        self.n2 = 0
        self.result = 0

    def add(self):
        self.result = self.n1 + self.n2
        return self.result
    def sub(self):
        self.result = self.n1 - self.n2
        return self.result

class Cal2(Cal1): #자식클래스(부모클래스 상속받음)
    def __init__(self):
        self.n1 = 0
        self.n2 =0
        self.result = 0

    def mul(self):
        self.result = self.n1 * self.n2
        return self.result

    def div(self):
        self.result = self.n1 / self.n2
        return self.result

calculator = Cal2() #매개변수가 없을 경우 공백 괄호로 생성자를 호출해서 만듬

print('생성자 속성에 접근해서 직접 값을 할당해주기 => 객체속성 변경')
calculator.n1 = 2
calculator.n2 = 3

print(f'덧셈결과 : {calculator.add()}')
print(f'곱셈결과 : {calculator.mul()}')

print()

print('사용자에게 값을 입력받아 함수 실행하기')
userInput1 = int(input('숫자1 입력:'))
userInput2 = int(input('숫자2 입력:'))

calculator.n1 = userInput1
calculator.n2 = userInput2

print(f'뺄셈결과 : {calculator.sub()}')
print(f'나눗셈결과 : {round(calculator.div(),1)}')
