#무한반복이란 반복문을 빠져나올 수 없는 경우로 whille문에서 조건식의 결고가 항상 True인 경우를 말함
flag= True
num =0
sum =0
while flag:
    num +=1
    sum+=num
    print('{}까지의 합은 {}입니다.'.format(num,sum))

    if sum >=100:
        flag = False

#위 아래 코드가 다른 이유는? -> 고민해보고 질문하기

# num =0
# sum =0
# while True:
#     num +=1
#     sum+=num
#     print('{}까지의 합은 {}입니다.'.format(num,sum))
#
#     if sum >= 100:
#         False

#하루에 독감으로 병원에 내방하는 환자 수가 50~100명 사이일때 -> random 함수를 이용하기
#누적 독감 환자수가 최초 1만명을 넘는 날짜?
import random
sum = 0
data=0
flag = True

while flag:
    patient = random.randint(50, 100)
    sum+=patient
    data+=1
    print('환자수 : {}, 날짜: {}일 이후, 누적 환자수 : {}'.format(patient, data, sum))

    if sum > 10000:
        flag = False