#톱니가 n1개 n2개 두개가 돌아갈 때 다시 맞물릴 때 까지의 회전수를 구하라(n2는 n1보다 크다)

#사용자가 입력한 톱니 개수
#최소 공배수로 나누어 줄 때 필요한 값
n1 = int(input('a톱니 개수 입력'))
n2 = int(input('b톱니 개수 입력'))

#사용할 변수 선언하기
gearA =0 #gearA의 톱니수
gearB =0 #gearB의 톱니수
leastNum =0 #최소공배수

#톱니 바퀴가 맞물리는 경우 => 최소 공배수 (각 톱니의 회전수는 최대공배수에서 사용자가 입력한 값으로 나눠주면 됨)
#횟수에 의한 반복이 아니기 때문에 for 대신 while 반복문을 사용

flag = True
while flag: #변수를 어떻게 설정하고 사용할 수 있는지 체크할 수 있는 문제
        #조건문 1
        # gearA가 더 작은 경우 안에서만 조건식을 작성
        if gearA !=0:
        #작은 톱니의 톱니개수가 0이 아닌 경우
                if gearA != leastNum:
                        gearA+=n1
                #gearA가 최소공배수가 아니라면 gearA에 n1 톱니수를 더해줌 > 왜?
                #설명 : gearA가 최소공배수가 될때까지 반복을 돌면서 계속 톱니개수가 더해져야 하기때문
                else:
                        flag = False
                #gearA가 최소공배수이면 반복문 멈추기
        else:
                gearA += n1
                #작은 톱니의 회전수가 0이라면, 톱니 개수만큼 더해줌

        # 조건문 2
        # gearB의 톱니가 더 큰 경우를 의미하는 조건식
        # gearB의 톱니가 0이 아니고 작은 톱니개수로 나누어 떨어질 경우 gearB가 가지고 있는 수가 최소공배수
        if gearB !=0 and gearB % n1 ==0:
                leastNum = gearB
        else:
                gearB += n2
print('최초 만나는 톱니 수(최소공배수):{}톱니'.format(leastNum))
print('gearA 회전수:{}회전'.format(int(leastNum/n1))) #int로 형변환을 하지 않으면 float 형태로 나오게 됨
print('gearB 회전수:{}회전'.format(int(leastNum/n2)))