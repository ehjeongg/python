n1 = int(input('gearA 톱니수 입력'))
n2 = int(input('gearB 톱니수 입력'))

gearA=0
gearB=0
leastNum=0

flag=True
while flag:
    if gearB != 0 and gearB % n1 ==0:
        leastNum = gearB
    else:
        gearB +=n2
    if gearA !=0:
        if leastNum == gearA:
            flag= False
        else:
            gearA +=n1
    else:
        gearA +=n1
print('최초 만나는 톱니 수(최소공배수):{}톱니'.format(leastNum))