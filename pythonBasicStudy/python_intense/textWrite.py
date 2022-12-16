#파이썬 텍스트 파일 다루기 -> open(), read(), write(), close() 함수를 다루게됨

#파일 열기함수사용 및 w -> 쓰기모드
file = open('E:/pythonTxt/test.txt', 'w') # w는 파일이 없으면 생성해주기도 하고, 기존 글자를 없애고 내용은 다 없애고 새로운 내용으로 덮음
#텍스트파일이 있는 디렉토리 주소/파일명, 'w'(쓰기모드) 형태로 작성
# 파일이 있는 경우 그 파일을 열고 없으면 새로 생성해줌

strCnt = file.write('hello text')
print(f'strCnt : {strCnt}')

file.close() # 파일 닫아주기

# >> 결과 : 해당 디렉토리 안에 test.txt파일이 생성되고, 그 안에 hello text 문자가 입력됨


print('실습 -------------------------------------------------------------------------------')

#시스템 시간과 일정을 텍스트 파일에 작성해보기
import time
lt = time.localtime()
print(lt)

# date = '[' + str(lt.tm_year) + '년' + str(lt.tm_mon) + '월' + str(lt.tm_mday) + '일' + ']' #lt.tm_year도 str이라 명시해줘야함
# print(date)

#위에 문장을 포맷형식으로 출력해보기(대,소문자 잘 구별해야함 안그럼 에러남)
dateStr = '[' + time.strftime('%Y-%m-%d %H:%M:%S %p') + ']' #H는 24시간제, I는 우리가 일반적으로 쓰는 시간
print(dateStr)


todo = input('일정을 입력하세요 : ')

filePython = open('E:/pythonTxt/today.txt', 'w')
contents = filePython.write(dateStr)
contents = filePython.write(todo)
file.close()
