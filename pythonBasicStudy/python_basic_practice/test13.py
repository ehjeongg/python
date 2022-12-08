# 정수 입력받고 합 / 홀수합 / 짝수합 / 팩토리얼 결과 받기

#변수 초기화를 하지 않았을 경우에 생기는 에러
#TypeError: unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'

#값 입력받기

num = int(input('정수를 입력하세요.'))

#사용할 변수 초기화
sum=0
even =0
odd=0
fac =1

for i in range(1, num+1): #1부터 입력한 정수까지의 범위
    sum +=i
    fac *=i #곱셈을 해야하기때문에 초기값이 1이여야됨
    #print(i) 범위 안에 있는 변수를 출력하고 싶으면 반복문 안에서 출력해야함
    if i%2==0: #짝수일 때
         even+=i #짝수들의 합
    elif i%2 !=0:
        odd+=i # 홀수들의 합
print('\n 합:{}, \n 홀수합:{}, \n 짝수합:{}, \n 팩토리얼:{}'.format(sum, odd, even, format(fac, ',')))

#end="" 형식을 사용하면 문장이 연결되서 출력되는 것을 알 수 있음
print(' 합:{}, 홀수합:{}, 짝수합:{}'.format(sum, odd, even), end="")
print(' 합:{}, 홀수합:{}, 짝수합:{}'.format(sum, odd, even))
#format 함수를 쓰면 단위가 큰 숫자를 편하게 볼 수 있음
#format(변수, ',') > format(변수, '컴마')
format(fac, ',')



