#실습 : 사용자가 문자보낼때 10글자 이상 sms, 초과 mms로 발송하는 프로그램을 예외처리를 이용해서 만들기

class smsException(Exception):
    def __init__(self, str):
        super().__init__(f'10글자 이내로 \'SMS\' 발송')

class mmsException(Exception):
    def __init__(self, str):
        super().__init__(f'10글자 초과로 \'MMS\' 발송')

userInput = input('문자를 입력하세요')
def sendmessage(str): #매개변수가 언제, 어떻게 쓰이는지 구별하고 쓰기
    if len(userInput) < 5:
        raise smsException(str)
    elif len(userInput) > 10:
        raise mmsException(str)

try:
    sendmessage(str)
except smsException as e1:
    print(e1)
except mmsException as e2:
    print(e2)