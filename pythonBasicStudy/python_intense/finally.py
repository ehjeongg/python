#finally : 예외발생과 상관없이 항상 실행한다 (예외가 발생하던, 하지 않던 무조건으로 실행하는 코드)
# => 외부 자원을 이용해서 작업을 할 때 등등

try:
    userInput = input('숫자 입력')
    num = int(userInput)
except:
    print('숫자가 아닙니다 - 에러발생')
else:
    if num %2 ==0:
        print('짝수입니다.')
    else :
        print('홀수입니다.')
finally: #try와 같은 구역의 라인에서 실행하게 됨
    print(f'입력된 데이터 : {userInput}') #예외여부 상관없이 항상 실행됨


print()
print('실습------------------------------------------------------------------------------------------------------------')
print()

evenList = []
oddList = []
floatList = []
userInputList = []
n = 1
while n < 6:
    try:
        userInput = input('숫자입력')  # 데이터를 처음 받을 때 모든 형태의 데이터를 받고
        num = float(userInput)  # 조건에 따라 분류할 수 있게 형변환을 시킴(정수/실수 모두 조건에 따라 분류해야되서 여기서는 씀)
    except:
        # userInputList.append(userInput) #해당 처리는 예외발생했을 경우 처리하는 것으로 항상 나오는 것이라면 finally에서 작성
        print('예외발생')
        print('정수 또는 실수를 재입력하세요')
        continue

    else:
        # 1. 실수 vs 정수 2. 홀수 vs 짝수 (조건문 작성 전에는 분류를 먼저 고려하기)
        # if print(isinstance(num, float)) == True: => 결과가 위에서 확인한 것이랑 다르게 나옴
        #     print('실수입니다.')
        #     floatList.append(num)

        if num - int(num) != 0:  # 실수 판단하는 방법
            print('실수입니다.')
            floatList.append(num)
        else:
            if num % 2 == 0:
                print('짝수입니다.')
                evenList.append(int(num))
            else:
                print('홀수입니다.')
                oddList.append(int(num))

        n += 1  # 예외조건을 해당되지 않은 정상 실행가능한 코드에서 처음 시작하는 조건문의 구역과 시작이 같아야 해당 조건을 타고 카운트를 하게됨

    finally:
        userInputList.append(userInput)
        # print(f'사용자 입력값 : {userInput}') #예외 발생 여부 상관없이 무조건 실행

print(f' evenList : {evenList}')
print(f' oddList : {oddList}')
print(f' floatList : {floatList}')
print(f' userInputList : {userInputList}')