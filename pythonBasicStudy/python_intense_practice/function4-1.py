#단리 / 복리 예금이자 계산 프로그램

# #내가 작성한 코드
# def formatnum(n) :
#     return format(n, ',')
#
# def simple(deposit, interest, period):
#     totalMoney = 0
#     totalRate = 0
#
#     for i in range(period):
#         totalRate +=deposit * (interest * 0.01) #백분율이라서 0.01 곱해줌
#
#     totalMoney = deposit + totalRate
#     return int(totalMoney)
#
#
# print('단리계산기')
# deposit = int(input('예치금 입력'))
# interest=float(input('이자율 입력'))
# period = int(input('기간 입력'))
#
# amount = formatnum(simple(deposit,interest,period))
#
#
# print('-' * 50)
# print(f'예치금 : {formatnum(deposit)}')
# print(f'이자율 : {interest}')
# print(f'기간 : {period}')
# print(f'{period}년 후 수령액 : {formatnum(amount)}')
# print('-' * 50)
# print('-' * 50)

def formatnum(n):
    return format(n, ',')

def single(d,r,t):
    # totalMoney = 0
    totalRate = 0

    for i in range(t):
        totalRate = d * (r* 0.01)


    totalMoney = d+ totalRate
    return int(totalMoney)

money = int(input('예치금 입력'))
rate = float(input('이율 입력'))
term = int(input('기간 입력'))
result = single(money, rate, term)
print('단리계산기')
print(f'예치금 : {formatnum(money)}')
print(f'이율 : {rate}')
print(f'기간 : {term}')
print(f'{term}년 후 예상 수령액 : {formatnum(result)}원 입니다.')

