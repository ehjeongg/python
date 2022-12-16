# w, a, x -> 쓰기 전용 형식
# w: 덮어 씌움
# a: 덧붙임(로그를 볼 수 있음)
# x: 파일이 존재하면 에러발생
# r - >읽기전용

# 소수 : 1과 자기자신외에 어떠한 수로도 나누어 떨어지지 않는 수
# 문제풀이 적용 -> 2부터 자기자신의 수 사이에 있는 어떤 수로도 나누어 떨어지지 않으면 된다


#텍스트파일 쓰기 흐름 파악하기
uri = 'E:/pythonTxt'
def write(n): # 매개변수
    file = open(uri + '/primeText.txt', 'a') # a와 w의 차이 구별 (w는 범위안에 가장 마지막번 소수만 출력됨)
    file.write(str(n)) # 파이썬 텍스트 파일은 문자열만 받기때문에 숫자만 입력할 경우 에러날 수 있어 형변환을 해줌
    file.write('\n') # 개행을 위해서 작성
    file.close()

userInput = int(input('0보다 큰 수 입력'))

#내가 쓴 코드
# for i in range(2, userInput+1):
#     if userInput % n == 0:
#         break
# if userInput % i !=0:
#     write
#         write(userInput)
#     print(userInput)


#강사 코드
for number in range(2, userInput+1): #이중 반복문이 필요한 이유 파악
    flag = True
    for n in range(2,number):
        if number % n ==0:
            flag = False
            break
    if flag:
        write(number) #소수를 쓰기파일에 저장하는 함수에 해당 number를 보내준다