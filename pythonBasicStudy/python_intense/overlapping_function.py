#중첩함수 : 함수 안에 또다른 함수가 있는 형태

def out_function():
    print('out function')

    def in_function(): #함수 안에 선언된 함수
        print('in function')

    in_function()
    # in_function()

out_function()
#함수 안에 정의된 중첩 함수를 외부에서 호출하면 NameError: name 'in_function' is not defined. 에러뜬(함수가 어딨는지 찾지 못한다는 소리)
# in_function()

print()
print('-' * 25, 'calculator 함수 만들기', '-' * 25)

#내가 쓴 코드 -> 실행 실패
# def cal(x,y, operator):
#     operator = int(input('계산방법 선택 : 1. 덧셈 2. 뺄셈'))
#     x = int(input('x값 입력'))
#     y = int(input('y값 입력'))
# 
#     if operator == 1:
#         def add():
#             result = x+y
#             print('덧셈결과 > {}'.format(result))
#     elif operator ==2:
#         def sub():
#             result = x-y
#             print('뺄셈결과> {}'.format(result))


#강사 코드
def cal(x, y, oper):

    def add():
        print('x+y ={}'.format(x + y))
    def sub():
        print('x-y ={}'.format(x - y))
    def mul():
        print('x*y ={}'.format(x * y))
    def div():
        print('x%y ={}'.format(x / y))
        
    if oper ==1:
        add()
    elif oper==2:
        sub()
    elif oper == 3:
        mul()
    elif oper == 4:
        div()

while True:
    oper = int(input('계산방법 입력 : 1. + 2. - 3. * 4. %  5. 종료'))

    if oper ==5:
        print('종료되었습니다')
        break
    elif oper != 5:
        x = int(input('x값 입력:'))
        y = int(input('y값 입력:'))
        cal(x, y, oper)