import math

#첫달에 200원을 받고 매월 이전 달의 2배씩 인상하기로함 / 12개월째에 받을 수 있는 돈은?
#-> 2배씩 12승을 먼저 구한다음, 돈의 단위가 100이라서 100을 나중에 곱해줘야함

firstMoney = 200
after12= int(((firstMoney*0.01)**12) * 100)
#after12 = (2 ** 12)*100
print(after12)
result = format(after12, ',') #한번 포맷으로 변경되게 되면 데이터형식은 string이 되게 된다
print(result, '원')

# / 나누기 % 나머지 //몫
