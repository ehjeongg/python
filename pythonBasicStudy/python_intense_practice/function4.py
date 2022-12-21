#재귀함수를 이용하여 팩토리얼 만들기

def fac():
    try:
        num = int(input('숫자를 입력하세요'))
        f = 1  #곱하기라서 변수 초기화시 1부터 시작
        for i in range(1,num+1):
            f *=i #f에다가 i를 계속해서 곱해줌
            print(i)

        print(f'num의 팩토리얼 : {f}')
    except:
        print('숫자만 입력하세요.')

fac()

print('-------------------------------------------------------------------------')
#강사예시 코드
def recursionFun(n): #재귀함수 function
    if n==1:
        return n
    return n  * recursionFun(n-1)


num = int(input('숫자를 입력하세요'))
print(recursionFun(num))


