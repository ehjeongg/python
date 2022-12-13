import prac1_module as unitConversion

cm = int(input('cm 입력:'))

if __name__ =='__main__': # 해당 코드를 써주지 않을 경우 prac2 파일을 import한 다른 실행파일에서 계속 실행될 수 있기 떄문에 작성해줌

    cm= int(input('cm 입력:'))

    result = unitConversion.cmToInch(cm)
    print('cm-> inch로 환산 : {}'.format(result))

    result = unitConversion.cmToM(cm)
    print('cm-> m로 환산 : {}'.format(result))

    result = unitConversion.cmToFt(cm)
    print('cm-> ft로 환산 : {}'.format(result))