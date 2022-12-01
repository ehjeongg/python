#난수를 이용해 컴퓨터가 발생한 숫자 맞추기
import random

computer = random.randint(1,10) #10까지의 정수 중 랜덤으로 1개 고르기
count = 0 #사용자가 숫자를 맞추기위해 시도한 횟수를 초기화
while True:
    count+=1 #반복문 한바퀴(게임 한번 실행할때) 돌 때 카운트 하기
    user = int(input('아무 숫자를 입력하여 맞춰보세요.')) #computer의 변수가 randint로 user도 int로 형 변환
    if computer > user:
        print('입력값이 난수보다 작습니다.')
    elif computer < user:
        print('입력값이 난수보다 큽니다.')
    else :
        print('빙고 정답입니다.')
        break


print('난수 : {}, 시도횟수: {}'.format(computer, count))

#다음에는 입력값이 이상값일 경우 예외처리도 생각하기

