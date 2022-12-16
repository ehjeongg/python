file = open('E:/pythonTxt/today.txt', 'r') # UnicodeDecodeError가 발생하면 encoding = 'UTF8' 추가

str = file.read() #파일에 있는 내용은 문자열로 받아옴
print(str)

file.close() #파일을 열었으면 닫아야함


# str = str.replace('변경전 문자', '변경후 문자', 몇번째) -> 텍스트 대체하는 함수


