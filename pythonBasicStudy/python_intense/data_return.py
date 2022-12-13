def cal(n1,n2):
    result = n1 + n2
    return result #cal() 함수에서 데이터를 return 함

returnValue = cal(1,2) #cal() 함수를 통해서 return된 값은 returnValue라는 변수에 할당됨

print('returnValue : {}'.format(returnValue)) #해당 변수를 원하는 형태로 print하면 값을 출력할 수 있음

#함수가 return을 만나면 실행을 종료한다

def dividedNum(n):
    if n % 2==0:
        return '짝수' #함수 실행종료 및 결과반환, 이후 조건문은 실행하지 않음
    else:
        return '홀수'
    #elif로 이 자리에 어떤 조건문이 또 온다고해도 위에서 return값이 있기 때문에 해당 코드라인은 실행되지 않음

returnVal = dividedNum(5) #인자로 받은 데이터 5는 매개변수를 통해서 dividedNum 함수에서 쓰이게 됨
print(dividedNum(5))
print('리턴값: {}'.format(returnVal))


#사용자가 cm를 입력하면 mm로 반환하는 함수

#내가 쓴 코드
def mmLength(): #입력값을 input으로 따로 받을때는 매개변수가 필요 없음 => 인자를 직접 전해줄 때만 매개변수 필요??
    userCm = int(input('cm입력:'))
    mm = userCm * 10
    mmValue = print('{}cm는 {}mm입니다.'.format(userCm, mm))
    return mmValue
mmLength()

#강사코드
def mmToCm(cm):
    result = cm*10
    return result
length = float(input('길이 입력:'))
mmV = mmToCm(length) #length로 입력받은 값은 def의 함수에서 매개변수 cm으로 전달됨
print(f'returnVal : {mmV}mm')

print()
print('-' * 100)

import random
#1부터 100사이의 난수(랜덤수) 중에서 홀수를 반환하는 함수
def oddNum():
    while True:
        num = random.randint(1, 100)  #랜덤함수의 범위 설정
        if num % 2 !=0:
            break
    return num
oddNum()
#여기에서는 함수만 호출한다고 출력이 되지 않음 -> 왜지? -> function3 파일에서는 출력이 되는데..?
#함수 안에 print 함수가 쓰여진 적이 없었기 때문에 반환값은 있으나 출력이 안되었던 것
print(f'내가 쓴 코드 : {oddNum()}')

def getOdd():
    while True:
        rNum = random.randint(1,100)
        if rNum % 2 !=0:
            break
    return rNum

#아래 형식은 변수만 사용할떄 가능
# print('random.randint : {}'.format(getOdd()))

#메서드(method)를 print하기 위해서는 f'' 형식을 사용해야함
print(f'random.randint : {getOdd()}')

