#객체 = 속성 + 기능
#객체는 클래스로부터 생성이 됨(클래스는 틀 / 객체는 실제 빵)
#객체지향 -> 모듈화와 코드 재사용에 유리(각 기능을 부품화(모듈화)함)

#속성 = 변수  / 기능 = 함수


class Car: #클래스 명은 대문자로 시장(변수와의 구별을 위함)

    #생성자와 속성을 선언(틀을 만드는 것)
    # def __init__(self, 매개변수1-속성, 매개변수2-속성) -> 형태 기억
    def __init__(self, col, vel): #self와 함께 매개변수를 나열
        # self.변수(클래스에서 온 객체 속성) =매개변수(__init__ 옆에 매개변수에서 받아온 매개변수) => 변수(속성)선언 -> 형태기억
        self.color = col
        self.velocity = vel

    #객체가 실행하는 동작(기능)선언
    def doStart(self): #안에 self는 왜 넣는건지? 매개 변수 역할?
        print('출발')

    def doStop(self):
        print('멈춤')

    def carInfo(self):
        print('color 정보=', self.color)
        print('velocity 정보=', self.velocity)

#객체는 클래스의 생성자(__init__ 메서드)를 호출한다.
# Car()라는 클래스를 호출하는 것은 함수 호출하는 것처럼 호출함

#속성을 init에 전달해줌으로써 속성을 초기화 하면서 생성자를 호출한다고 말함

#생성된 object(객체2개) - class안에 있는 기능도 이용할 수 있음
car1 = Car('red' , 100) #속성을 초기화해주는 매개변수
car2 = Car('blue' , 200)

print('car1에 대한 정보 ')
car1.carInfo()
car1.doStop()
print()
print('car2에 대한 정보 ')
car2.carInfo()
car2.doStop()
print()
print('car1에 대한 정보 변경한 후 ')
#속성에 접근해서 속성값을 바꾸는 방법
car1.color = 'pink'
car1.carInfo()