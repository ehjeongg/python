#함수 선언
def addCal():
    n1 = int(input('a 입력'))
    n2 = int(input('b 입력'))

    print(f'n1+n2 = {n1+n2}')

#함수 호출(함수 안에 print함수를 사용했는지 확인필요)
addCal()

#함수 호출 시 아래 두개의 차이 구별하기 (return을 사용했을때, print를 사용했을때)
def weather():
    print('오늘 날씨 추움')
weather()
# weather()

def today():
    return '오늘 무슨 요일임 헬요일임'
print(today())
#today()



