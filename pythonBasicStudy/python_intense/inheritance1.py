class NormalCar:

    def drive(self):
        print('[NormalCar] drive() called!!')


    def back(self):
        print('[NormalCar] back() called!!')

# TurboCar(NormalCar) 작성을 통해서 상속을 받을 수 있게됨 터보카는 상속받은 drive,back + 기존 turbo 총 3가지의 기능을 가질 수 있게됨
class TurboCar(NormalCar):
    def turbo(self):
        print('[TurboCar] Turbo() called!!')
        
myTurbo = TurboCar() #TurboCar 클래스를 이용하여 객체 생성

#원래 터보에 있던 기능
myTurbo.turbo()

#NormalCar로부터 상속받은 기능
myTurbo.drive()
myTurbo.back()

print('-' * 50, '실습')
#덧셈, 뺄셈 기능이 있는 클래스를 만들고 곱셈 나눗셈을 상속받아서 곱셈 나눗셈 기능 추가해보기

