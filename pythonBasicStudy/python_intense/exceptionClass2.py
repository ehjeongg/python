#raise 키워드를 이용하면 예외를 발생시킬 수 있다

# def div(n1,n2):
#     if n1 or n2 != 0:
#         return n1 / n2
#     else:
#         raise Exception('0으로는 나눌 수 없습니다.')
#
# x = int(input('숫자1 입력'))
# y = int(input('숫자2 입력'))
#
# try:
#     div(x,y)
# except Exception as e:
#     print(f'Exception : {e}')

print('--------------------------------------------------------------------------------------------')

#실습 : 사용자가 문자보낼때 10글자 이상 sms, 초과 mms로 발송하는 프로그램을 예외처리를 이용해서 만들기


def sendmms(message):
    if len(message) > 10:
        raise Exception('10글자 초과로 MMS로 발송됩니다.', 1)
    else:
        print('SMS 발송되었습니다.')

def sendsms(message):
    if len(message) <= 10:
        raise Exception('10글자 이내로 SMS로 발송됩니다.', 2)
    else:
        print('MMS 발송되었습니다.')

message = input('문자메시지를 입력하세요.')

try:
    sendmms(message)
except Exception as e:
    print(f'e: {e.args[0]}') #args는 arguments의 약자(인자의 요소들 각각을 가리킴)

    if e.args[1] ==1:
        sendmms(message)
    elif e.args[1] ==2:
        sendsms(message)