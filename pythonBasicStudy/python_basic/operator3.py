import random
import operator #같은 디렉토리 안에 예약어나 같은 모듈 이름이 있으면 해당 파일 내용으로 결과가 출력됨

#random과 operator 모듈을 사용해서 10부터 100까지의 난수 중
#십의 자리와 일의 자리가 3의 배수인지 판단하는 코드를 작성해라

randomInt = random.randint(10, 100) #10에서 100사이의 랜덤수 하나를 뽑음

num10 = operator.floordiv(randomInt, 10) #몫만 구하는 함수
num1 = operator.mod(randomInt, 10) #나머지만 구하는 함수

print(f'난수 : {randomInt}')
print(f'십의 자리 : {num10}')
print(f'일의 자리 : {num1}')
print(f'십의 자리가 3의 배수이다. : {operator.mod(num10,3)==0}')
print(f'일의 자리가 3의 배수이다. : {operator.mod(num1,3)==0}')