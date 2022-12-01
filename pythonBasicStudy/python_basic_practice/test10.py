#상수도 요금 계산기
# kind = int(input('업종선택 1. 가정 2. 대중 3. 공업'))
# amount = int(input('사용량 입력'))
#
# if kind ==1:
#     charge = amount * 540
# elif kind ==2:
#     if amount <= 50:
#         charge =amount * 820
#     elif amount > 50 and amount <= 300:
#         charge =amount * 1920
#     elif amount > 300:
#         charge = amount*2400
# else :
#     print('잘못 입력하셨습니다.')
# print('사용량 \t: 요금\t' ) #\t을 넣어주면 열을 맞춰줌
# print(amount, ':',  f' {charge}원')


# 2부제 5부제의 개념을 몰랐음(2부제는 짝홀수 번호판으로 판단, 5부제는 번호판 1의 자리를 5로 나눠서 같은 경우 운행 정지)
import datetime

today = datetime.datetime.today()
print(today)
day = today.day
print(day) #오늘의 날짜만 구할 수 있음

mise = int(input('미세먼지 수치입력'))
car = int(input('차량 선택 : 1. 일반 2. 영업'))
number = input('번호판 입력시 운행가능')
if mise > 150:
    if car == 1:
        print('2부제 실시, 운행 불가')
    elif car ==2:
        print('영업용은 예외적 차량 운행 가능')
elif mise <=150:
    print('5부제 실시 운행가능 ')