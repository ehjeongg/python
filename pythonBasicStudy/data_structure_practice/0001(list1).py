import math
#1부터 사용자가 입력한 숫.자.까.지.의. 약수와 소수를 리스트에 각각 담고 출력하라
#사용자가 입력한 숫자까지의(ex. 10을 입력했으면, 1부터 10까지의 약수와 소수를 구분하라는 얘기)

# 약수 : 어떤 수를 나누어 떨어지게 하는 수
# 소수 : 1과 자기 자신만을 약수로 가지는 수
#1은 소수도 아니고 합성수도 아니다.

user = int(input('1보다 큰 아무 숫자를 입력해라'))
y = [] #리스트를 선언해줌
s= []
for i in range(1, user+1):
    if i ==1: #1은 소수도 합성수도 아니기 때문에 먼저 약수 리스트에 넣어줌
        y.append(i)
    else:
        if user % i ==0: #user list에 있는 수(i)로 나누었을때 딱 나누어 떨어지는 수는 약수임
            y.append(i)
#print 함수를 반복문 안에 쓰면 결과값이 반복됨
print('입력한 수 : {}'.format(user))
print('{}의 약수: {}'.format(user, y))
#내풀이 ↓
# for num in range(2, user+1): #소수는 자기자신과 1만을 약수로 가지는 수
#     for n in range(2, num):
#         if num % n ==0:
#             s.append(user)
#         n+=1
#
#     print('{}의 소수: {}'.format(user, s))

for num in range(2, user+1):
    flag = True
    for n in range(2, num): #나누어 인덱스를 돌아다니는 num을 나눠서 떨어지는 수를 표현
        if num % n ==0:
            flag = False
        break # 소수가 아니라면 반복문 빠져 나오기
    if flag:
        s.append(num) #반복문이 실행되는 동안에 나누어 떨어지면 소수리스트에 담아주기

print('{}까지의 소수: {}'.format(user,s))
