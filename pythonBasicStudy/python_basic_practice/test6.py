#상품가격과 지불 금액을 입력하면 거스름돈을 주는 프로그램(거스름돈은 지폐와 동전의 개수를 최소화하고 1원단위 절사)
#지폐 : 5만, 1만, 5천, 1천
#동전 : 500, 100, 10

price = int(input('상품가격 입력'))
cost = int(input('지불 금액 입력'))
change = cost - price #거스름돈
change = (change // 10)*10 #1원 단위는 절사 -> 10으로 나눈 몫에 다시 10을 곱해주기

list=[50000, 10000, 5000, 1000, 500,100,10]

cnt50000=0
cnt10000=0
cnt5000=0
cnt1000=0
cnt500=0
cnt100=0
cnt10=0

if cost > price:
    while True:
        for i in list:
            temp = price % i
            if temp > 50000:
                cnt50000+=1
            elif temp > 10000:
                cnt10000 +=1
            elif  temp > 5000:
                cnt5000 +=1
            elif  temp > 1000:
                cnt1000 +=1
            elif  temp > 500:
                cnt500 +=1
            elif  temp > 100:
                cnt100 +=1
            elif  temp > 10:
                cnt10 +=1

print('거스름돈: {}, 5만원 : {}, 1만원:{}, 5천원:{}, 1천원:{}, 500원:{}, 100원:{}, 10원:{}'
      .format(change,cnt50000, cnt10000, cnt5000, cnt1000, cnt500, cnt100, cnt10))




