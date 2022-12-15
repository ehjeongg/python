#Exception class : 예외 담당 클래스

num1 = int(input('input numer1: '))
num2 = int(input('input numer2: '))

try:
    print(f'num1 / num2 = {num1 / num2}')
except:
    print('0으로 나눌 수 없습니다.') # 개발자가 직접 입력한 문구

print(f'num1 * num2 = {num1 * num2}')
print(f'num1 - num2 = {num1 - num2}')
print(f'num1 + num2 = {num1 + num2}')


try:
    num1 = int(input('input numer1: '))
    num2 = int(input('input numer2: '))
except Exception as e:
    print(f'exception: {e}')
    num1 = 10
    num2 = 20

try:
    print(f'num1 / num2 = {num1 / num2}')
except ZeroDivisionError as e:
    print(f'exception: {e}')

print(f'num1 * num2 = {num1 * num2}')
print(f'num1 - num2 = {num1 - num2}')
print(f'num1 + num2 = {num1 + num2}')


def divCalculator(n1, n2):

    if n2 != 0:
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        raise Exception('0으로 나눌 수 없습니다.')


num1 = int(input('input numer1: '))
num2 = int(input('input numer2: '))
divCalculator(num1, num2)

def divCalculator(n1, n2):

    if n2 != 0:
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        raise Exception('0으로 나눌 수 없습니다.')


num1 = int(input('input numer1: '))
num2 = int(input('input numer2: '))

try:
    divCalculator(num1, num2)
except Exception as e:
    print(f'Exception: {e}')
