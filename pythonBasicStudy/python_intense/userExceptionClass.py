#사용자 Exception Class 예외 처리하는 클래스를 사용자가 직접 만들어서 사용

class NotUseZeroException(Exception): #기존 Exception에서 해당 클래스를 상속받고
    def __init__(self, n): #매개변수와 생성자를 만들어서
        super().__init__(f'{n}은 사용할 수 없습니다') #부모 클래스의 생성자 강제호출하고 원하는 내용 출력하게 하기
                                                   #Exception이라는 클래스가 에러 내용을 보여주는 클래스이기 때문
 

def div(x, y):
    if y == 0:
        raise NotUseZeroException(y) #어떤 매개변수를 받고 에러를 raise시킬 것인지 생각
    else:
        print('x % y = {}'.format(x/y))

x = int(input('x입력'))
y = int(input('y입력'))

try:
    div(x, y)
except NotUseZeroException as e:
    print(e)



print('실습 ----------------------------------------------------------------------------')
# 관리자 암호를 입력하고 상태에 따라 예외처리하는 클래스 만들기
# 암호길이 5미만 : lengthShortError
# 암호길이 10초과 : lengthLongError
# 암호 잘못된 경우 : worngError

class lengthShortError(Exception):
    def __init__(self, str): # 매개변수로 들어오는 암호(str)과 비교해야함
        super().__init__(f'5미만 길이가 짧습니다.')

class lengthLongError(Exception):
    def __init__(self, str):
        super().__init__(f'10초과 길이가 깁니다.')

class worngError(Exception):
    def __init__(self, str):
        super().__init__(f'잘못된 암호입니다.')

# 강사 코드
userInput = input('암호를 입력하세요.')

try:
    if len(userInput) <5 :
        raise lengthShortError(userInput)
    elif len(userInput) > 10:
        raise lengthLongError(userInput)
    elif userInput != 'pwd1234':
        raise worngError(userInput)
    elif userInput == 'pwd1234' :
        print('암호가 해제되었습니다.')
except lengthShortError as e1:
    print(e1)
except lengthLongError as e2:
    print(e2)
except worngError as e3:
    print(e3)


#내가 쓴 코드
# userInput = input('암호를 입력하세요')
# pwd = 1234
# def pwd():
#     if userInput < 5:
#         raise lengthShortError
#     elif userInput > 10:
#         raise lengthLongError
#     elif userInput != pwd
#         raise worngError
#
#
# try:
#     pwd() #여기에 해당하는 함수를 실행해보는 것
# except:





