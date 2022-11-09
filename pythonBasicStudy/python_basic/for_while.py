#for문을 사용할때는 횟수에 의한 반복일때,
#while문을 사용할때는 조건에 의한 반복일때 사용해야 간결함

#1부터 10까지 더하는 경우_for문 사용
sum = 0
for i in range(1,11):
    sum+=i
print('for문 사용 -> sum : {}'.format(sum))

print('-' *50)
#1부터 10까지 더하는 경우_while문 사용
result=0
n=1
while n < 11:
    n += 1
    result+=n
#프린트 들여쓰기에 따라서도 출력물이 달라짐(while문 안에 있느냐, 밖에 있느냐의 차이)
    print('while문 사용 -> sum:{}'.format(result))
print('-' * 50)
print('while문 사용 -> sum:{}'.format(result))
