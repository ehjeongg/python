#예외란? 문법적인 문제는 없으나 실행 중 발생하는 예상하지 못한 문제

#에러 : 소프트웨어적으로 처리하기 어려운 문제
#예외 : 문법상 문제는 없으나 예상치 못한 문제


# - 예외(에러)가 발생하는 경우 -
# print(10/0) -> 에러발생 :ZeroDivisionError: division by zero

# print(int('dkfksdf')) -> 에러발생 : ValueError: invalid literal for int() with base 10: 'dkfksdf'

lists = [1,2,3,4,5,6]
# print(lists[6]) -> 에러발생 : IndexError: list index out of range


#예외처리 : 예상하지 못한 에외가 프로그램 전체 실행에 영향이 없도록 처리
#1. try ~ except 예외가 발생 예상 구문을 try ~ except로 감싼다

n1 = 10; n2 = 0
try:
    print(n1/n2) #-> 예외가 발생할 만한 부분
except:
    print('예상치 못한 문제 발생')
    print('다음 프로그램 정상 실행')
print(n1*n2)
print(n1+n2)
print(n1-n2)

#실습 : 사용자로부터 숫자 5개 입력받고 숫자아니면 에외처리 하는 프로그램

# +plus for문과 while문의 차이 찾아내기
nums = []
for i in range(1,6):
    try:
        num=int(input('숫자입력'))
    except:
        print('예외발생') #예외 발생했을때는 i에 카운트를 하지 않음
        continue
    nums.append(num)
    i+=1

print(f'nums : {nums}')


numbers = []
n=1
while n < 6:
    try:
        user = int(input('숫자입력'))
    except:
        print('예외발생') #예외가 발생했을때는 별도로 n에 카운트를 하지 않음
        continue #카운트를 하면 안되기 때문에 continue(다음으로 넘어간다는 소리)

    #예외에 걸리지 않으면 정상적으로 실행될 코드
    numbers.append(user)
    n+=1
print(f'numbers : {numbers}')

#2. try except ~ else는 else 영역안에 실행되어야 할 구문을 써주면 된다.

nums = []
n = 1
while n < 6:
    try:
        num = int(input('input number: '))
    except:
        print('예외 발생')
        continue
    else: #정상적으로 실행되어야 하는 코드
        if num % 2 == 0:
            nums.append(num)
            n += 1
        else:
            print('입력한 숫자는 홀수 입니다.', end='')
            print('다시 입력 하세요.')
            continue

print(f'nums: {nums}')

