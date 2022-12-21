#영수증 출력하는 프로그램

childPrice = 18000 #24개월 미만
infantPrice = 25000 #만12세 미만
adultPrice = 50000 #12세 이상
specialDC = 50 #국가유공 할인

def formatnum(n):
    return (n,',') #-> 숫자 알아보기 쉽도록 형식화
def recept(c1,c2,i1,i2,a1,a2):
    cp = c1 * childPrice
    cp_dc = int(c1 * childPrice * 0.5)
    print(f'유아 {c1}명, 요금: {formatnum(cp)}원')
    print(f'할인대상 유아 {c2}명, 요금 : {formatnum(cp_dc)}원')

    i1 = i1 * childPrice
    i2_dc = int(i1 * childPrice * 0.5)
    print(f'소아 {c1}명, 요금: {formatnum(cp)}원')
    print(f'할인대상 소아 {i2}명, 요금 : {formatnum(i2_dc)}원')

    ap = a1 * adultPrice
    ap_dc = int(a2 * adultPrice * 0.5)
    print(f'성인 {a1}명 요금: {formatnum(ap)}원')
    print(f'성인 할인 대상 {a2}명 요금: {formatnum(ap_dc)}원')

    # print(f'총 {매개변수 모두 더하기}명')
    # print(f'총 {formatnum(가격 모두 더하기)}원')



print('----------------------------------------------------------------------------------------------')
#강사예시코드

# def formatedNumber(n): #금액을 사용하는 것으로 단위를 만들어줌
#     return format(n, ',')
#
# def printAriPlaneReceipt(c1, c2, i1, i2, a1, a2):
#
#     print('=' * 40)
#     cp = c1 * childPrice
#     cp_dc = int(c2 * childPrice * 0.5)
#     print(f'유아 {c1}명 요금: {formatedNumber(cp)}원')
#     print(f'유아 할인 대상 {c2}명 요금: {formatedNumber(cp_dc)}원')
#
#     ip = i1 * infantPrice
#     ip_dc = int(i2 * infantPrice * 0.5)
#     print(f'소아 {i1}명 요금: {formatedNumber(ip)}원')
#     print(f'소아 할인 대상 {i2}명 요금: {formatedNumber(ip_dc)}원')
#
#     ap = a1 * adultPrice
#     ap_dc = int(a2 * adultPrice * 0.5)
#     print(f'성인 {a1}명 요금: {formatedNumber(ap)}원')
#     print(f'성인 할인 대상 {a2}명 요금: {formatedNumber(ap_dc)}원')
#
#     print('=' * 40)
#     print(f'Total: {formatedNumber(c1 + c2 + i1 + i2 + a1 + a2)}명')
#     print(f'TotalPrice : {formatedNumber(cp + cp_dc + ip + ip_dc + ap + ap_dc)}원')
#     print('=' * 40)
#
#
# print(f'childPrice(24개월 미만)\t\t: {formatedNumber(childPrice)}원')
# print(f'infantPrice(만12세 미만)\t\t: {formatedNumber(infantPrice)}원')
# print(f'adultPrice(만12세 이후)\t\t: {formatedNumber(adultPrice)}원')
# print(f'국가 유공자 및 장애우 할인\t\t: {specialDC}%')
# print()
#
# childCnt = int(input('유아 입력: '))
# specialDCChildCnt = int(input(f'할인대상 유아 입력: '))
#
# infantCnt = int(input('소아 입력: '))
# specialDCInfantCnt = int(input(f'할인대상 소아 입력: '))
#
# adultCnt = int(input('성인 입력: '))
# specialDCAdultCnt = int(input(f'할인대상 성인 입력: '))
#
#
# printAriPlaneReceipt(childCnt, specialDCChildCnt, #각각 매개변수
#                 infantCnt, specialDCInfantCnt,
#                 adultCnt, specialDCAdultCnt)
#



