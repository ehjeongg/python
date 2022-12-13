#모듈이란? 함수가 선언(특정 기능을 가지고 있는)되어 있는 파이썬 "파일"이다.
#(이미 만들어져있는 기능으로 사용자가 쉽게 사용할 수 있음)

#내부:파이썬 설치기 기본으로 설치된 모듈 / 외부:별도 설치후 사용할 수 있는 모듈 / 사용자 모듈 : 사용자가 직접 만들 모듈

#모듈을 사용하기 위해서는 import를 사용해서 쓸 수 있음
import random
rNum = random.randint(1,10)
print(f'rNum: {rNum}')

#random모듈에서 .sample함수를 쓰면 범위 안에서 n개의 랜덤 숫자를 반환
rNums = random.sample(range(1,101), 10) #출력값은 list 형태로 나옴
print(f'rNums : {rNums}')


