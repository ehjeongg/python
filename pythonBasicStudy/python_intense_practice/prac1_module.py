def cmToInch(n):
    return round(0.393 * n, 3) #소수점 3자리까지만 표현

def cmToM(n):
    return round(10 * n, 3)

def cmToFt(n):
    return round(0.032 * n, 3)

# #prac1이라는 모듈이 main일때만 아래 print를 실행
# if __name__ == '__main__':
#     print(f'cm -> inch : {cmToInch(10)}')
#     print(f'cm -> inch : {cmToM(10)}')
#     print(f'cm -> inch : {cmToFt(10)}')



# "if __name__ == '__main__': " => 이 코드를 써주지 않을 경우 import한 다른 실행파일에서도 계속 실행이 됨
print(f'cm -> inch : {cmToInch(10)}')
print(f'cm -> inch : {cmToM(10)}')
print(f'cm -> inch : {cmToFt(10)}')