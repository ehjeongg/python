#추상클래스 : 어떤 상속관계에 있을때 상위클래스가 하위클래스에게 이 메서드는 꼭 하위에서 생성하라고 강요함

#오버라이딩은 상위에서 구현되어 있는 메서드를 하위에서 재정의 한 것이지만,
#추상 클래스는 상위에서 메서드 선언만 되어있고 하위에서 구현하게 강요하는 것이다.

# 추상 클래스는 선언만 하고 상속 받는 클래스에서 알아서 필요한대로 수정해서 쓰게끔 하는 것

#추상 클래스를 사용하기 위해 import 하는 모듈
from abc import ABCMeta
from abc import abstractmethod

class AirPlane(metaclass=ABCMeta):

    @abstractmethod
    def flight(self): #함수 선언만 하고 별도의 정의는 하지 않음
        pass

    def forward(self):
        print('전진!!')

    def backward(self):
        print('후진!!')

#Airliner클래스와 fighterPlane 클래스 모두 AirPlane 클래스를 상속받고
class Airliner(AirPlane):

    def __init__(self, c):
        self.color = c

    def flight(self): #flight라는 같은 함수를 사용하는데
        print('시속 400km/h 비행!!')


class fighterPlane(AirPlane):

    def __init__(self, c):
        self.color = c

    def flight(self): #선언된 같은 함수를 필요에 따라 수정하여 사용
        print('시속 700km/h 비행!!')


ap1 = Airliner('red')
ap1.flight()
ap1.forward()
ap1.backward()


ap2 = fighterPlane('blue')
ap2.flight()
ap2.forward()
ap2.backward()
