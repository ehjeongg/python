#lambda 함수를 쓰면 함수 선언이 간단해짐(함수가 간단해서 람다를 써야할 경우, 코드가 더 간결해짐)
def cal(x,y):
    return x+y
returnValue = cal(10,20)
print(f'returnValue:{returnValue}')

#람다함수를 이용한 경우
calculator = lambda n1,n2: n1+n2 #함수가 간단해서 간결해진 코드(2줄로 표현하는 것을 1줄로 표현가능)
returnValue = calculator(10,20)
print(f'returnValue:{returnValue}')


#삼각형,사각형,원의 넓이를 구하는 람다함수 만들기

#lambda함수 선언
getTri = lambda n1,n2 : (n1+n2) * 0.5
gerSqu = lambda n1,n2 : n1*n2
getCir = lambda r1 : r1 * r1 * 3.14

#매개변수에 쓰일 값 입력받기
width = int(input('가로입력'))
height = int(input('세로입력'))
redius = int(input('반지름입력'))

#함수에 입력값을 전달해서 출력되는 값 변수에 담기
triValue = getTri(width, height)
squValue = gerSqu(width, height)
cirValue = getCir(redius)

#변수에 담긴 출력될 값 print하기
print(f'삼각형넓이 : {triValue}')
print(f'사각형넓이 : {squValue}')
print(f'원의 넓이 : {cirValue}')
