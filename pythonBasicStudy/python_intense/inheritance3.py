#다중 상속(2개 이상의 클래스를 상속받는다)
#다중상속은 남발하지 않고 필요할 경우에만 사용(변수, 클래스명이 헷갈리면 프로그램이 꼬일 수 있음)

class Car01:
    def drive(self):
        print('drive() method')

class Car02:
    def turbo(self):
        print('turbo() method')

class Car03:
    def fly(self):
        print('fly() method')

class Car(Car01, Car02, Car03): #상속받을 클래스명을 나열한다
    def __init__(self):
        pass

#모든 기능을 사용할 수 있는것을 알 수 있음
myCar = Car()
myCar.drive()
myCar.turbo()
myCar.fly()

#실습 : 기본 계산기와 심화계산기 클래스를 만들고 둘의 클래스를 상속받아 Calculator 클래스를 만들고 사용해보기

class BasicCalculator:
    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

class DevelopCalculator:
    def mod(self, n1, n2): #나머지만 구하기
        return n1 % n2

    def flo(self, n1, n2): #몫만 구하기
        return n1 // n2

    def exp(self, n1, n2): #제곱을 구하기
        return n1 ** n2

class Calculator(BasicCalculator, DevelopCalculator):
    def __init__(self):
        print('2개 클래스를 상속받은 계산기')

cal = Calculator()
print(f' cal.mul(2,4) : {cal.mul(2,4)}')
print(f' cal.add(1,4) : {cal.add(1,4)}')
print(f' cal.mod(4,5) : {cal.mod(4,5)}')
print(f' cal.exp(2,3) : {cal.exp(2,3)}')

