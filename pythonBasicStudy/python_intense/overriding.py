#오버라이딩 : 하위클래스에서 상위클래스로 메서드를 재정의한다

class Robot:
    def fire(self):
        print('총알 발사') #부모 클래스에서 총알을 발사하고

class NewRobot:
    def fire(self): #자식 클래스에서 부모클래스가 사용하는 같은 함수명으로 다른 것을 정의하는 것이 overriding
        print('레이저발사')

r = NewRobot() #새로운 생성자를 만들어서
r.fire() #fire라는 함수를 사용하게 하니 -> 총알이 아닌 레이저로 변경됨

#삼각형 넓이 구하는 클래스 만들고 오버라이딩으로 출력결과에 단위 붙여주기

class Tri:
    def __init__(self, n1, n2):
        self.width = n1
        self.height = n2

    def getArea(self):
        area = (self.width * self.height) / 2
        return area

    def print(self):
        print(f'부모클래스 - 삼각형 넓이:{self.getArea()}')

class NewTri(Tri):
    def __init__(self, n1, n2): #자식 클래스에서의 매개변수는 부모 클래스의 매개변수를 포함하고 있어야함(부모매개변수+자식매개변수)
        super().__init__(n1,n2) #부모의 매개변수만 super()로 가져옴

    def print(self):
        print('< 자식클래스 > ')
        print(f'가로길이 : {self.width}')
        print(f'세로길이 : {self.height}')

        print(f'삼각형 넓이 : {super().getArea()}cm2') #getArea는 나 자신에게 없느 것이라 super().함수명 을 통해서 기능을 씀

tri = Tri(2,3) #클래스에서 객체 생성할 때 필요한 매개변수와 함께 세팅을 해야함
tri.print()

print()
newTri = NewTri(1,2)
newTri.getArea()
newTri.print()

