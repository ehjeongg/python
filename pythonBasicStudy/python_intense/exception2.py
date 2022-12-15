# 실습 : 사용자로부터 숫자 5개 입력받아 짝수, 홀수, 실수 구분해서 각 리스트에 저장하는 프로그램

# *실수인지 판별하기 => isinstance(변수명, float) / 정수판별 => isinstance(변수명, int)
# >> print(isinstance(변수명, float))
# >> 결과 : True

# n=2
# print(isinstance(n, float))
# d=3.444
# print(isinstance(d, float))

evenList=[]
oddList = []
floatList=[]
n=1 # while문이 돌아다는 처음 시작을 선언해줌
while n < 6:
    try: #사용자가 숫자를 입력하지 않는 경우를 고려
        num = float(input('숫자 입력')) #실수 입력도 받고 있기때문에 float으로 형변환 하고 필요한 경우 밑에서 int로 변환

    except:
        print('예외발생')
        print('정수 또는 실수를 재입력하세요')
        continue

    else:
        #1. 실수 vs 정수 2. 홀수 vs 짝수 (조건문 작성 전에는 분류를 먼저 고려하기)
        # if print(isinstance(num, float)) == True: => 결과가 위에서 확인한 것이랑 다르게 나옴
        #     print('실수입니다.')
        #     floatList.append(num)

        if num - int(num) !=0:  # **실수를 판단하는 방법
            print('실수입니다.')
            floatList.append(num)
        else:
            if num%2 ==0:
                print('짝수입니다.')
                evenList.append(int(num))
            else:
                print('홀수입니다.')
                oddList.append(int(num))

        n+=1 #예외조건을 해당되지 않은 정상 실행가능한 코드에서 처음 시작하는 조건문의 구역과 시작이 같아야 해당 조건을 타고 카운트를 하게됨

print(f' evenList : {evenList}')
print(f' oddList : {oddList}')
print(f' floatList : {floatList}')






