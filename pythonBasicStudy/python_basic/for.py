# 반복문이란?
# 특정 실행을 반복하는 것으로
# 반복문을 사용하며 프로그래밍이 간결하고 유지 보수가 쉬워진다
# 대량메일 또는 문자 발송 / 인사말 반복 / 노래 반복 재생 / 타이머 등

# 횟수에 의한 반복 -> for
# 조건에 의한 반복 -> while

for i in range(2,10): #for의 범위에서는 마지막 숫자 포함하지 않음
    print('-' * 30)
    print(f'[{i}단 곱셈]')
    for j in range(1,10):

        print('{} * {} ={}'.format(i, j, (i*j)))

# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{} * {} = {}".format(i, j, i * j))

for var in range(5): #0부터 4까지의 숫자를 반복함
    print('hi')

#사용자가 입력한 숫자에 맞는 구구단을 출력
user = int(input('숫자 입력'))
print(f'{user}단 곱셈')
for g in range(2,10):
    print('{} * {} = {}'.format(user, g, user*g))