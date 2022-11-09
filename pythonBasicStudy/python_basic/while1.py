#while문 사용 방법
# 변수 설정(초기화)
# while 조건식: (조건식이 True일때 반복을 실행함)
#     실행문

#들여쓰기로 해당 조건에 대한 실행을 판단
endNum = 10
n=0
while n<endNum:
    print(n)
    n+=1

#1부터 100까지의 정수 중 2의 배수와 3의 배수를 구분해서 출력해봐라
n=1
while n < 101:
    n += 1 #무한루프에 빠지지 않도록 않게 함
    if n%2 == 0:
        print('{}은 2의 배수이다.'.format(n))
    elif n%3 ==0:
        print('{}은 3의 배수이다.'.format(n))

#while가지고 구구단 만들기
gugu = int(input('사용자 입력'))
n=1
while n<10:
    result = gugu * n
    print('{} * {} = {}'.format(gugu, n, result))
    n+=1

