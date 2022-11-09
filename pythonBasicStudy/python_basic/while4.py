#반복 실행 중 break를 만나면 반복문을 빠져나옴

num=0
while True: #-> 평생 반복되는 것
    print('hello')

    num+=1
    if(num>5):
        break #조건에 해당하면 반복문 탈출하기

#1부터 100까지 정수를 더할 때, 합계가 100이 넘는 최초의 정수찾기

#10의 팩토리얼을 계산하는 과정에서 결과값이 50을 넘을 때의 숫자
result=1
num =0
for i in range(1,11):
    result *= i
    if result>50:
        num=i
        break
print(f'50을 넘을 때 숫자 : {num}, 결과값 : {result}')

#강아지 체중 2.2키로 넘으면 이유식 중단 / 한번 이유식을 먹을때 체중이 70g 증가 / 예상되는 이유식 날짜(현재 체중 800g)

max = 2200
date = 0
current = 800
while True:
    current +=70
    date+=1
    if current> 2200:
        break
print(f'날짜:{date}')