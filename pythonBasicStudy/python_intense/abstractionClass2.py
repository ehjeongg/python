#실습 :

#추상 클래스를 사용하기 위해 import 하는 모듈
from abc import ABCMeta
from abc import abstractmethod

class Calculator(metaclass=ABCMeta): #추상 메서드 사용하기 위해 부모클래스에서 선언

    @abstractmethod
    def add(self, x,y):
        pass
    @abstractmethod
    def sub(self, x, y):
        pass
    @abstractmethod
    def mul(self, x, y):
        pass
    @abstractmethod
    def div(self, x, y):
        pass

class ChildCalculator(Calculator):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

childCal = ChildCalculator()
childCal.add(10, 20)
childCal.sub(10, 20)
childCal.mul(10, 20)
childCal.div(10, 20)

class DeveloperCalculator(Calculator):

    def add(self, x, y):
        print(x + y)

    def sub(self, x, y):
        print(x - y)

    def mul(self, x, y):
        print(x * y)

    def div(self, x, y):
        print(x / y)

    def mod(self, x, y):
        print(x % y)

    def flo(self, x, y):
        print(x // y)

devCal = DeveloperCalculator()
devCal.mul(2,3) #def 함수 옆에 매개변수가 있기에 여기에서 숫자를 넣어주는 것
devCal.add(10, 20)
devCal.sub(10, 20)
devCal.mul(10, 20)
devCal.div(10, 20)
devCal.mod(10, 20)
devCal.flo(10, 20)
