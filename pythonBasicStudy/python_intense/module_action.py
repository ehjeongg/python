import  module_user
#파일명.함수명(매개변수) 형태로 원하는 데이터를 넣어 함수의 결과를 알 수 있음


#로또 번호 생성하기
num = module_user.getLotto() #모듈 파일명.함수명(매개변수)
print(f'로또번호 : {num}')


#계산기
module_user.add(10,20)
module_user.sub(10,20)
module_user.mul(10,20)
module_user.div(10,20)


#입력한 문자열 거꾸로 출력하기
str = input('문자열 입력')
reverString =module_user.rever(str)
print(reverString)

