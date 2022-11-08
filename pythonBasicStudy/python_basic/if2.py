#중첩 조건문 (조건문 안에 조건문이 존재)

comuting = int(input('출퇴근 대상 1.yes 2.no'))

if comuting == 1:
    print('교통수단을 선택하라')
    trans = int(input('1. 지하철 2. 도보 3. 차량'))
    if trans ==1:
        print('지하철 : 세금 20프로 감면')
    elif trans ==2:
        print('도보 : 세금 40프로 감면')
    elif trans ==3:
        print('차량 : 세금 5프로 감면')
    else:
        print('잘못 입력')
elif comuting ==2:
    print('세금변동 없음')
else:
    print('잘못입력')