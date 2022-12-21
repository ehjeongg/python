#단리 / 복리 예금이자 계산 프로그램

def formatnum(n) :
    return format(n, ',')

def simple(deposit, interest, period):
    result = 0
    totalRate = 0

    for i in range(period):
        totalRate +=deposit * (interest * 0.01) #백분율이라서 0.01 곱해줌

    result = deposit + totalRate
    return int(result)

    print('-' * 50)
    print('-' * 50)
    print(f'예치금 : {deposit}')
    print(f'이자율 : {interest}')
    print(f'기간 : {period}')
    print(f'{period}년 후 수령액 : {formatnum(result)}')
    print('-' * 50)
    print('-' * 50)
