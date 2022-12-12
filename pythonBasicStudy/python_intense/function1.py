#함수(내장함수와 사용자함수가 있음)
#함수 사용의 목적 -> 특정 기능의 재사용

def add(x,y): #함수의 이름과 사용할 변수명을 선언
    return x+y
print(add(1,2)) #함수의 이름과 변수를 넣어 출력

def multi(q,w):
    result = q*w #함수가 어떤 기능을 하는지 선언
    return (f'곱셈결과(q*w) : {result}')
print(multi(4,5))

#매개 변수가 있는 경우
name = input('이름입력')
def userName(name): #name은 매개변수
    # print('{}님 안녕하세요'.format(name))
    return f'{name}님 안녕하세요'
print(name)
print(userName(name)) #출력할때 함수의 이름과 매개변수를 넣어줌

#위에 코드가 모두 출력되고 난 후에 입력값을 받음
#print(addName()) 이 함수는 매개변수가 없이 함수 안에서 입력값을 받기 떄문


#매개 변수없이 사용자 지정 함수 안에서 값을 입력받는 경우
def addName():
    n1 = input('이름입력1')
    n2 = input('이름입력2')
    # result('{}, {} 환영합니다'.format(n1,n2))
    output = ('{},{} 환영'.format(n1,n2)) #출력하고 싶은 내용
    # print(output) #직접 함수안에서 출력값을 써도 되고
    return output #return값을 명시해줘도 됨( %print를 쓸 경우 none값이 중간에 발생할 수 있음)

print(addName()) #함수 호출을 하는 것인데 함수 안에서 print를 사용하지 않았을 경우

# addName() #함수 안에 print 함수를 사용한 경우 함수명으로만 호출이 가능

