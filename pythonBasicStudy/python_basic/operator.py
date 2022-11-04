import math
print(math.sqrt(5)) #항상 2의 제곱근만 구하는 점 주의
print(math.pow(2,3))


num1=3
num2=4
result = num1 ** num2 #pow() 함수로 사용 가능
#거듭제곱을 할 때는 별 표시를 2개 한다
#제곱근을 구할때는 '** 분수' 로 작성한다
print(result) #3의 4승(3*3*3*3의 결과)

#2의 2제곱근
result = 2**(1/2)
print('%.2f' %result)

#2의 3제곱근
result = 2 **(1/3) #sqrt() 함수로 사용 가능
print('%.3f' %result)

var1 = 2
var2 = 5

compareResult = var1 > var2 #비교결과는 True, false로 나옴
print(compareResult)

#문자열 비교는 같다와 같지 않다만 비교가 가능하다
#알파벳 입력시 아스키 코드를 출력하는 함수 ord()
inputAlphabet= input('문자 입력')
print('{} : {}'. format(inputAlphabet, ord(inputAlphabet)))

#아스키 코드 입력시 알파벳 출력하는 코드
inputAscii = int(input('아스키 입력'))
print('{} : {}'.format(inputAscii, chr(inputAscii)))


