#계산기 함수 만들기 -> 함수사용 이유 : 재사용을 위해서

def cal():
    #함수 시작시 기능별 번호 안내
    print('1.덧셈 2.나머지 3.몫 4.거듭제곱 0.종료')

    try : #실행해볼 코드
        while True: #종료번호 눌리지 않는 이상 기능 계속 반복

            #필요한 값 입력받기
            choice = int(input('기능선택'))

            #조건에 따라 프로그램 실행 여부가 달라지는 경우 if문을 따로 쓰기
            if choice == 0:
                print('종료가 선택되어 종료되었습니다.')
                break

            #필요한 값 입력받기
            num1 = int(input('x 입력'))
            num2 = int(input('y 입력'))

            # 조건에 따라 프로그램 실행여부가 달라지는 경우 if문을 따로 쓰기
            if choice == 1:
                print(f'x+y = {num1+num2}')
            elif choice == 2:
                print(f'mod(x,y) = {num1%num2}')
            elif choice == 3:
                print(f'x//y = {num1//num2}')
            elif choice == 4:
                print(f'x**y = {num1**num2}')

    except : #프로그램 비정상 실행시 처리될 내용
         print('숫자만 입력이 가능합니다')

#함수 실행해보기
cal()

# print('----------------------------------------------------------------------------------------')
# #강사 예시코드
# def add(n1, n2):
#     return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# def mul(n1, n2):
#     return n1 * n2
#
# def div(n1, n2):
#     return n1 / n2
#
# def mod(n1, n2):
#     return n1 % n2
#
# def flo(n1, n2):
#     return n1 // n2
#
# def exp(n1, n2):
#     return n1 ** n2
#
# while True:
#
#     print('-' * 60)
#     selectNum = int(input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.나머지, 6.몫, 7.제곱승, 8.종료 '))
#     if selectNum == 8:
#         print('Bye~')
#         break
#
#     num1 = float(input('첫 번째 숫자 입력: '))
#     num2 = float(input('두 번째 숫자 입력: '))
#
#     if selectNum == 1:
#         print(f'{num1} + {num2} = {add(num1, num2)}')
#
#     elif selectNum == 2:
#         print(f'{num1} - {num2} = {sub(num1, num2)}')
#
#     elif selectNum == 3:
#         print(f'{num1} * {num2} = {mul(num1, num2)}')
#
#     elif selectNum == 4:
#         print(f'{num1} / {num2} = {div(num1, num2)}')
#
#     elif selectNum == 5:
#         print(f'{num1} % {num2} = {mod(num1, num2)}')
#
#     elif selectNum == 6:
#         print(f'{num1} // {num2} = {flo(num1, num2)}')
#
#     elif selectNum == 7:
#         print(f'{num1} ** {num2} = {exp(num1, num2)}')
#
#     else:
#         print('잘못 입력했습니다. 다시 입력하세요.')
#
#     print('-' * 60)

