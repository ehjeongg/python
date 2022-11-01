#데이터 타입 float 실수 bool 논리형

num = 10
print(type(num))

num = str(num) #형변환을 해줌
print(type(num)) #str으로 타입이 변환됨

#true = 1  false = 0

#빈문자 != 공백 문자
#공백 문자는 공백이라는 데이터가 있는 것

# true으
var1 = 'true'
var1 = bool(var1)
print(var1)

var2 = 'false'
var2 =bool(var2) #문자열을 논리형으로 바꿀 때 데이터가 있냐 없냐 기준으로 true/ false를 반환함
print(var2)

print(var1 + var2)

var3 = 'adf'
var3 = bool(var3) # 논리형으로 데이터 타입이 바뀜
print(type(var3)) #결과는 bool로 나옴

userInput = input('입력해라') #input() 괄호안에 안내문을 넣으면 됨
print(userInput)
print(type(userInput))# input으로 받는 것은 모두 str임

secondInput = int(input('숫자만 입력하세요'))
print(secondInput)
pirnt(type(secondInput))

