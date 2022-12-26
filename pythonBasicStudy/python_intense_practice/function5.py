#등차수열의 항과 항까지의 값 구하기
def sequenceCal(n1, r, n):

    valueN = 0
    sumN = 0
    i =1

    while i <= inputN:
        if i ==1:
            valueN = n1
            sumN += valueN
            print(f'{i}번째 항의 값 : {valueN}')
            print(f'{i}번째 항까지의 합 : {sumN}')
            i+=1
            continue

        valueN *= r
        sumN +=valueN
        print(f'{i}번째 항의 값 : {valueN}')
        print(f'{i}번째 항까지의 값 : {sumN}')
        i+=1 #무한반복에 빠지지 않도록 함

inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))


sequenceCal(inputN1, inputR, inputN)
print('-' * 50)
