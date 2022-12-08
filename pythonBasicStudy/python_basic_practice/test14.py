#별 만들기
#format 함수와 end=""(두 개 이상의 문장을 한 줄로 연결해줌)을 각각 잘 이욯하면 코드가 간결해짐

#1번모양
print( '-' * 30, '1번 모양')
for h in range (1,6): #별의 개수 범위 설정
    for h1 in range (h):
        print('*', end='') #한 줄안에 찍혀야할 별들은 개행을 하지 않음
    print('') #한줄이 다 작성되고 나면 개행을 해줌

#2번모양(1번의 거꾸로된 모양)
print( '-' * 30, '2번 모양')
#for i in range(6): #0부터 5까지의 범위
for a in range(1,6):
    for b in range (6-a-1): #의미생각하기
        print(' ', end='')
    for c in range(a):
        print('*', end='')
    print('')

#3번 모양
print( '-' * 30, '3번 모양')
for d in range(5, 0, -1): #range를 설정하는 방식 다시 기억하기
    for e in range (d):
        print('*', end='')
    print('')

#4번 모양
print( '-' * 30, '4번 모양')
for f in range(5,0,-1):
    for g in range(6-f-1):
        print(' ', end='')
    for h in range(f):
        print('*', end='')
    print() # == print('') 동일한 표현

#5번 모양
print( '-' * 30, '5번 모양 -> 내가 푼 코드 (모양이 조금 다름)' )
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print() #줄 바뀔때 개행
    if i==5:
        for i in range(4,0,-1): #range 범위 range(5,0,-1) -> range(4,0,-1) 변경 후 모양을 맞춤
            for j in range (i):
                print('*', end='')
            print()

print( '-' * 30, '5번 모양 -> 강사 예시 코드')
for i in range(1,10):
    if i < 5:
        for j in range(i):
            print('*', end='')
    else: #5보다 큰 경우에 해당되는 조건문
        for j in range(10-i):
            print('*', end='')
    print()

#6번 모양
print( '-' * 30, '6번 모양')
for i in range(1,6):
    for j in range(i):
        print(' ', end='')
    print('*')

print( '-' * 30, '6번 모양 - 강사코드')
for i in range(1,6):
    for j in range(1,6):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print() #내가 푼 것과 어느부분이 다른지 확인필요

#7번 모양
print( '-' * 30, '7번 모양')
for i in range(5, 0, -1): #범위를 생각하고
    for j in range(i):
        print(' ', end='') #어떤것이 먼저 출력될지
    print('*') #어느 부분에서 무엇을 출력하고 개행(줄바꿈)이 필요한지

#마름모 모양도 찍어보기
