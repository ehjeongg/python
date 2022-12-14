#얕은복사 : 객체 주소를 복사하는 것으로 객체 자체가 복사되지 않음
#깊은 복사 : 객체 자체를 복사하는 것으로 또 하나의 객체가 만들어짐

class TemCls:

    def __init__(self, n, s):
        self.number = n
        self.str = s

    def printClsInfo(self):
        print(f'self.number: {self.number}')
        print(f'self.str: {self.str}')


# 얕은 복사
tc1 = TemCls(10, 'Hello')
tc2 = tc1

tc1.printClsInfo()
tc2.printClsInfo()

tc2.number = 3.14
tc2.str = 'Bye'

#두개의 변수가 같은 객체를 바라보고 있기 때문에 하나의 속성을 변경하면 다른 것도 변경됨
tc1.printClsInfo()
tc2.printClsInfo()



# 깊은 복사
import copy #copy모듈을 이용

tc1 = TemCls(815, 'Hello')
tc2 = copy.copy(tc1) #copy모듈의 copy()라는 함수로 사용

#객체를 깊은 복사 한것으로 현재는 속성값 동일
tc1.printClsInfo()
tc2.printClsInfo()

#tc2의 속성을 변경해줌
tc2.number = 6.6
tc2.str = 'hi'

#출력된 것을 보면 각자 다른 속성을 가지고 있음
tc1.printClsInfo()
tc2.printClsInfo()

print()
print('리스트 복사', '-' * 50)
print()

# 리스트 깊은 복사
scores = [9, 8, 5, 7, 6, 10]
scoresCopy = []


scoresCopy = scores #얕은 복사를 했기 때문에 메모리 주솟값이 같은 것을 알 수 있음
print(f'id(scores): {id(scores)}') #id(변수명) -> 해당 객체 또는 리스트의 아이디 값을 알 수 있음
print(f'id(scoresCopy): {id(scoresCopy)}')

#깊은 복사를 이용하기
for s in scores:
    scoresCopy.append(s) #깊은 복사와 같은 역할을 함
#id값이 다른 것을 알 수 있음
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')


scoresCopy.extend(scores) #초기화된 scoresCopy 리스트에 scores를 확장하면 깊은 복사와 같은 역할을 함
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')


scoresCopy = scores.copy() #copy 모듈을 이용한 깊은복사
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')


scoresCopy = scores[:] # scores[:]-> 처음부터 끝까지 슬라이싱을 하는 것으로 리스트 전체를 할당하는 것이라고 볼 수 있음
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')




