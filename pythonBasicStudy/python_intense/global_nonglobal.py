#전역변수 : 함수 밖에서 선언된 변수로 함수 내/외부에서 모두 사용가능 하지만 함수 안에서 수정할 수 없음
#(새로운 값이 또 할당되는 것일뿐 like 동명이인)

#지역변수 : 함수안에서 선언된 변수로 함수안에서만 사용가능한 변수

print('전역변수', '-'*60)

num = 10 #전역변수
def printNum():
    num = 20 #함수 안에서만 사용할 수 있는 지역변수
    print(f'num : {num}')
printNum() #함수를 호출했기때문에 함수 안에 있는 num인 20을 출력
print(f'num : {num}') #함수 밖에서 선언된 변수를 호출해서 10을 출력

print()
print('global 변수', '-'*60)

#global
#전역변수를 함수안에서 다른 데이터로 수정하고 싶을 때 사용하는 변수
num = 10 #전역변수
def printNum():
    global num_out #전역변수를 함수안에서 수정해서 사용하겠다는 의미
    num_out = 20
    print(f'num : {num_out}')
printNum() #함수를 호출했기때문에 함수 안에 있는 num인 20을 출력
print(f'num : {num_out}') #함수 밖에서 선언된 변수를 호출해서 10을 출력

#방문객 수를 카운트하는 함수

totalVisit =0 #전역변수
def count():
    global totalVisit #글로벌 선언으로 전역변수를 함수 내에서 수정하겠다고 선언

    totalVisit +=1 #전역 변수의 값을 +1 해준 값으로 계속 수정함
    print('누적방문:{}'.format(totalVisit))

count() #1번째 방문
count() #2번째 방문
count() #3번째 방문