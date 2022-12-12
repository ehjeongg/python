#톱니가 n1개 n2개 두개가 돌아갈 때 다시 맞물릴 때 까지의 회전수를 구하라(n2는 n1보다 크다)

#n1,n2는 사용자에게 입력받기 / n2가 n1보다 크다는 가정하에 있음

n1 = int(input('A톱니 개수 입력:'))
n2 = int(input('B톱니 개수 입력:'))
gearA =0
gearB=0
leastNum=0
#flag변수를 사용하지 않을 때 왜 반응을 안하는 것인지
flag = True
while flag:
    if gearB !=0 and gearB % n1 ==0:
        # gearB = leastNum
        leastNum = gearB #변수는 오른쪽에서 왼쪽으로 할당하기 때문에 순서도 중요함
    else:
        gearB +=n2

    if gearA != 0:
        if gearA == leastNum:
            flag = False  # gearA가 최소공배수일 경우 반복문 멈춤
        else:
            gearA += n1  # gearA에 n1만큼의 톱니개수를 더해줌(반복문을 계속 돌아야 하기 떄문)
    else:
        gearA += n1

print('최초 만나는 톱니 수(최소공배수):{}톱니'.format(leastNum))
#회전수
print('gearA 회전수:{}회전'.format(int(leastNum/n1))) #int로 형변환을 하지 않으면 float 형태로 나오게 됨
print('gearB 회전수:{}회전'.format(int(leastNum/n2)))