#조건문의 형태
# if 조건문:
#     실행문
# else:
#     실행문

# if 조건문:
#    pass -> 실행문이 아직 정해지지 않은 경우 사용
# else:
#    pass

#q. 소수점 첫 번째 자리에서 반올림하는 프로그램
floatNum = float(input('소수 입력'))

if floatNum - int(floatNum) >= 0.5:
    print('올림 : {}'.format(int(floatNum)+1)) #조건문은 참일때만 실행됨
else:
    print('버림 : {}'.format(int(floatNum)))

