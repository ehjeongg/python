#클래스에서 생성자를 호출하여 객체를 만들면 메모리에 저장됨
#객체 : 변수명 = 객체  (변수에는 객체의 메모리 주소가 할당되는 것 )

class Robot:
    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight

    def printRobotInfo(self):
        print(f'color: {self.color}')
        print(f'height: {self.height}')
        print(f'weight: {self.weight}')

rb1 = Robot('red', 200, 80)
rb2 = Robot('blue', 100, 20)
#rb3은 rb1의 메모리주솟값만 할당된 것 (객체가 카피된 것이 아님) -> 변수 2개가 1개의 객체 메모리 주소를 바라보고 있는것
rb3=rb1
#(.copy()라는 함수를 이용하면 실체 객체를 똑같이 카피해줌 2개의 변수와 2개의 객체인 것)

rb1.printRobotInfo()
print()
rb2.printRobotInfo()
print()
rb3.printRobotInfo()

#속성 바꿔보기
rb1.color = 'gray'

print('속성 바꿔보기')
rb1.printRobotInfo()
print()
rb2.printRobotInfo()
print()
rb3.printRobotInfo() #rb3의 속성값도 변경된 것을 알 수 있음

print('-' * 50 , '실습')



#국어, 영어, 수학 점수를 입력받아 리스트에 저장하고 원본을 유지한 상태로, 복사본을 만들어 과목별 점수를 10% 올렸을 경우 평균출력 해보기
import copy
list=[]
kor = int(input('국어 입력'))
math = int(input('수학 입력'))
eng = int(input('영어 입력'))
list.append(kor)
list.append(math)
list.append(eng)
#print(f'list: {list}') #리스트 원본

# 복사한 리스트
listCopy =[]
# listCopy = listCopy.extend(list)
listCopy = list.copy()
#print(listCopy)

#카피한 리스트에서 요소들을 10퍼센트씩 올려주기
for i, score in enumerate(listCopy): #enumerate : index와 요소가 같이 리스트를 돌게됨
    result = score * 1.1
    if result > 100:
        result == 100
    else:
        listCopy[i] = result
# print('카피해서 10퍼 올린 리스트 : ' , listCopy)

# 반복문에 사용되는 변수 초기화
beforeSum=0
afterSum = 0

#원본 점수의 합계 구하기
for i in list:
    beforeSum +=i
print(beforeSum) #=> sum함수를 이용해서 리스트 요소의 합계를 간단하게 구할 수 있음 ex.sum(list) : 원본리스트 합계

#카피 점수의 합계 구하기
for i in listCopy:
    afterSum += i
print(afterSum)  #=> sum함수를 이용해서 리스트 요소의 합계를 간단하게 구할 수 있음 ex.sum(listCopy) : 카피리스트 합계


print(f'원본 점수의 평균 : {beforeSum / len(list)}')
print(f'카피 점수의 평균 : {afterSum / len(listCopy)}')


#강사코드
scores = [int(input('국어 점수 입력: ')),
          int(input('영어 점수 입력: ')),
          int(input('수학 점수 입력: '))]

# print(scores)

copyScores = scores.copy()

for idx, score in enumerate(copyScores):
    result = score * 1.1
    copyScores[idx] = 100 if result > 100 else result

print(f'이전 평균: {round(sum(scores) / len(scores), 2)}')
print(f'이후 평균: {round(sum(copyScores) / len(copyScores), 2)}')