# speed = int(input('속도 입력 : '))
#
# if speed > 50 :
#     print('과속! 속도 줄여')
# elif speed < 50:
#     print('안전운전하시네')

# 난수(random int)를 이용해서 가위바위보 만들기
import random #랜덤함수를 발생시킬 때 사용하는 모듈

computer = random.randint(1,3)
user = int(input('1 가위 2 바위 3 보 : 입력하세요'))
if computer == 1:
    com='가위'
elif computer  == 2:
    com = '바위'
elif computer  ==3:
    com = '보'

if user == 1:
    userKor='가위'
elif user  == 2:
    userKor = '바위'
elif user  ==3:
    userKor = '보'

print('computer:{}, user:{}'.format(com,userKor))

if computer == user:
    print('무승부')
elif (computer ==1 and user ==3) or \
    (computer ==2 and user==1) or \
    (computer ==3 and user ==2): #역슬래시로 긴 문장을 자를 수 있음
    print('computer 승 ,user 패')
else :
    print('user 승, computer 패')

# 카운트 제한해서 반복분도 써보기 5회 이상시 게임 자동 종료
