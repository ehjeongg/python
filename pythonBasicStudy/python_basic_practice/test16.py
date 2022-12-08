#톱니가 n1개 n2개 두개가 돌아갈 때 다시 맞물릴 때 까지의 회전수를 구하라

n1 = int(input('a톱니 개수 입력'))
n2 = int(input('b톱니 개수 입력'))

#사용할 변수 선언하기
gearA =0
gearB =0
leastNum =0 #최소공배수

#톱니 바퀴가 맞물리는 경우 = > 최소 공배수 (각 톱니의 회전수는 최대공배수에서 사용자가 입력하 값을 나눠주면 됨)
#횟수에 의한 반복이 아니기 떄문에 for 대신 while 반복문을 사용

flag = True
while flag: #변수를 어떻게 설정하고 사용할 수 있는지 알 수 있는 문제
        if gearA !=0:
                if gearA != leastNum:
                        gearA+=n1
                else:
                        flag = False
        else:
                gearA += n1
        if gearB !=0 and gearB % n1 ==0:
                leastNum = gearB
        else:
                gearB += n2

print('최초 만나는 톱니 수(최소공배수):{}톱니'.format(leastNum))

