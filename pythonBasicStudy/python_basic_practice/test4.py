
select = int(input('영어 1번 한글 2번 선택하세요'))

while True:
    if(select == 1):
        print('영어메뉴 입니다.')

    elif(select == 2):
        print('한글 메뉴 입니다. ')
    else:
        print('잘못입력했습니다.')
    break

    #-> 반복문으로 계속 손님을 받다가 손님 5명이 초과되면 영업종료 하기

