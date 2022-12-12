#함수 안에서 또 다른 함수 호출하기
def fun1():
    #아래 코드들으 위에서부터 차례로 호출됨
    print('fun1 호출')
    fun2()
    print('fun2 호출 후에') #호출되는 순서중 가장 마지막

def fun2():
    print('fun2 호출')
    fun3()

def fun3():
    print('fun3 호출')

fun1() #fun1() 함수를 실행한 후 fun2()를 실행하고 마지막에  "print('fun2 호출 후에')" 실행함

print('-' * 60)

#customer이 매개변수로써 앞으로 받을 데이터를 대변함
#홍길동이라는 데이터는 인수라고 함

def greet(customer): #인수를 3개 받고싶으면, 매개 변수 또한 3개를 선언해야함
    print(f'{customer}고객님 안녕하세요.')

greet('홍길동')


#매개변수가 2개일때 인수를 1개 넘기면, missing error가 발생함

print('-' * 60)

#매개 변수 개수가 정해지지 않은 경우
def printNum(*numbers): #*numbers가 모든 매개변수를 통틀음
    print(type(numbers)) #<class 'tuple'> / 별 표시를 뺀 경우 : <class 'int'> 일반적인 숫자로만 인자를 받음
    for i in numbers:
        print(i, end='')


printNum(1)
printNum(1,2,3,4,5)
printNum(1,2,3,4,5,6,7,7,8,8)

print('-' * 60)


def printFruits(*fruits):
    print(type(fruits))
    for i in fruits:
        print(i)
printNum('과일', '사과', '바나나')


print('-' * 60)

def score():
    kor = int(input('국어입력'))
    eng = int(input('영어입력'))
    math = int(input('수학입력'))
    list = [kor, eng, math]

    sum = kor + eng + math
    avg = sum / len(list)

    print('총점 : {}, 평균 : {}'.format(sum, round(avg, 1)))

score()
score()
score()
