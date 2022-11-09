#반복 실행 중 continue를 만나면 실행을 생략하고 다음 반복문으로 넘어가라는 뜻

#1,2번 같은 결과

#1번
for i in range(100): #range(100)은 0부터 99까지의 범위를 말함
    if i % 7 !=0:
        continue #이하 반복 실행 생략 / 다시 처음의 반복으로 돌아감
    print('{}는 7의 배수 '.format(i))

print('-' * 70)
print('-' * 70)

#2번
for i in range(100):
    if i % 7 ==0:
        print('{}는 7의 배수 '.format(i))


#1부터 100까지의 정수 중 3과 7의 공배수(공통배수 : 3 and 7의 배수를 구하기)와
#최소 공배수를 출력하라
#1번 내가 풀이한것
min =0 #최소공배수의 변수를 선언하고 초기화해줌
for i in range(1,101):
    if i % 3 ==0 and i %7==0:
        print(f' 공배수 : {i}') #공배수 구하기
        if min == 0: #초기화 값으로 조건을 걸고 한번만 실행될 수 있게함
            min=i
print(f'최소공배수 : {i}')

#2번
minNum = 0
for j in range(1,101):
    if j %3 !=0 or j % 7!=0:
        continue
    print('공배수:{}'.format(j))

    if minNum==0:
        minNum=j
print('최소공배수 : {}'.format(minNum))
#----------------------------------------------------------
# else: -> 이 else가 가지고 있는 if는 어디에서 시작 된 것인가 고민하고 질문하기
#     print('최소공배수 : {}'.format(j))