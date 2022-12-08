#버스 운행정보가 있을때 2대 이상의 버스가 정차하는 시간대 출력
#A,B버스 운행정보 : 6시 첫차, 23시 막차 / A:15분 간격, B: 13분 간격
#C버스 운행정보 : 6시20분 첫자, 22시 막차/ C:8분 간격
#=> 최소 공배수의 개념(한 변수를 원하는 수로 나누었을때 동시에 나누기한 값이 ==0일 경우를 의미)

A =15
B=13
C=8

totalMin = 60 * 17 #하루 17시간 운행함

for i in range (totalMin+1):
    if i < 20 or i > (totalMin-60): #A,B만 운행하는 경우
        if i % A ==0 and i % B ==0: #범위 안에서 반복해서 돌고 있는 변수(시간을 의미)를 고정되어있는 변수 A로 나눠야함
            print('a와 b버스 동시정차', end='')
            hour = 6+ i//60
            min = i%60
            print('{}시 {}분'.format(hour, min))
    else: #A, B, C 모두 운행
        if i % A ==0 and i % B ==0:
            print('a와 b모두 동시정차', end='')
            hour = 6 + i // 60
            min = i % 60
            print('{}시 {}분'.format(hour, min))
        elif i % A ==0 and i % C ==0:
            print('a와 C모두 동시정차', end='')
            hour = 6 + i // 60
            min = i % 60
            print('{}시 {}분'.format(hour, min))
        elif i % B ==0 and i % C ==0:
            print('B와 C모두 동시정차', end='')
            hour = 6 + i // 60
            min = i % 60
            print('{}시 {}분'.format(hour, min))

