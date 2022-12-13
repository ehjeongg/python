import random

#로또번호를 얻는 함수
def getLotto():
    result = random.sample(range(1,45), 6) #range 범위 설정이 없으면 에러남

    return result

#계산기 기능 함수
def add(x,y):
    print(f'x+y :{x+y}')

def sub(x, y):
    print(f'x-y :{x - y}')

def mul(x, y):
    print(f'x*y :{x * y}')

def div(x, y):
    print(f'x%y :{x / y}')

#문자열을 거꾸로 반환하는 함수
def rever(str):
    reversedString = '' #rever 함수에서 사용할 변수 선언

    for i in str:
        reversedString = i + reversedString
        #print(reversedString)

    return reversedString

#rever('abcd') #함수가 출력되는 규칙 생각하기