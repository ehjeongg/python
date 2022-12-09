#윤년 계산기 프로그램
#윤년 조건 :
# 1. 연도가 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않는 경우
# 2. 연도가 400으로 나누어 떨어지는 경우
#확인할 수 있는 횟수제한 추가해보기
#숫자 이외의 것을 입력한 경우 재입력 시키기 > 입력값의 데이터형식 확인하는 함수 이용하기

#잘못된 반복문의 사용 (입력값도 while 문 안에 있어야함 / 횟수의 조건 또한 따로 적어야 함)
# year = int(input('년도 입력 : '))
# n=0
# flag = True
# while flag:
#     for n in range(11):
#         if n<6:
#             if (year %4 == 0 and year % 100 !=0) or year%400==0:
#                 n += 1
#                 print('윤년이다 - 조건1 만족')
#             else:
#                 n += 1
#                 print('평년이다')
#         else:
#             break



# flag = True
# n=0 #반복되지 않는 변수등은 while문 같은 반복문 밖에서 선언하기
# print('총 5번 평/윤년을 확인할 수 있습니다.')
# while flag:
#     # n = 0 -> n=0이라는 변수 선언이 반복문 안에 들어오면 다른 조건과 같이 반복되기때문에 무한루프에 돌게됨
#     year = int(input('년도 입력 : '))
#     n+=1
#     if (year %4 == 0 and year % 100 !=0) or year % 400==0 : #여러가지 조건식을 한줄에 사용하는 방법
#         n += 1
#         print( '{}년은 윤년이다'.format(year))
#
#     else:
#         n += 1
#         print( '{}년은 평년이다'.format(year))
#     if n > 5:
#         flag = False
#         print('\n확인 가능한 5회권 모두 소진되었습니다. ')


# #정상 코드
# flag = True
# n=0
# year=0
# print('총 5번 평/윤년을 확인할 수 있습니다.')
# while flag:
#     if n < 5:
#         year = int(input('년도 입력 : '))
#         n += 1
#
#         if (year %4 == 0 and year % 100 !=0) or year % 400==0 : #여러가지 조건식을 한줄에 사용하는 방법
#             n += 1
#             print( '{}년은 윤년이다'.format(year))
#
#         else:
#             n += 1
#             print( '{}년은 평년이다'.format(year))
#     else:
#         flag = False
#         print('\n확인 가능한 5회권 모두 소진되었습니다. ')



#정상코드
n=0
year=0
print('총 5번 평/윤년을 확인할 수 있습니다.')
while True:
    if n < 5: #가장 처음 횟수가 n=0부터 시작하기 때문에 5미만의 숫자가 주어지는 것 / n=0부터 1회이기 때문 -> n = 0,1,2,3,4(총 5회)
        year = int(input('년도 입력 : '))
        if (year %4 == 0 and year % 100 !=0) or year % 400==0 : #여러가지 조건식을 한줄에 사용하는 방법
            n += 1
            print( '{}년은 윤년이다'.format(year))
        else:
            n += 1
            print( '{}년은 평년이다'.format(year))
    else:
        print('\n확인 가능한 5회권 모두 소진되었습니다. ')
        break
