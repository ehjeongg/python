#enumerate() 함수를 이용하면 인덱스와 아이템(요소)을 열거할 수 있음

sports = [1, 'a', '34ddf', 'adf']
for i in range(len(sports)):
    print('{} : {}'.format(i, sports[i]))

for idx, value in enumerate(sports):
    print('{} : {}'.format(idx, value))

print('-'* 45)

# enumerate()는 문자열에도 적용가능
str = 'hello world'
for index, string in enumerate(str):
    print('{}, : {}'.format(index,string))
    #원하는 변수명 두개를 붙이면, 처음의 변수에는 index값이 부여됨

# Q. 사용자가 입력한 문자열에서 공백의 개수를 출력하시오
text = input('문자를 입력하세요')
cnt = 0
for idx, value in enumerate(text):
    if value == ' ':
        cnt+=1

print('사용자가 입력한 공백개수:{}'.format(cnt))