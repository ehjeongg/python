#with ~ as : 파일닫기(close)를 생략할 수 있다

# uri = 'E:/pythonTxt/'
# with open(uri + 'apple.txt', 'w') as f:
#     f.write('python study')
#
# with open(uri + 'apple.txt', 'r') as f:
#     print(f.read())

print('실습 ---------------------------------------------------------------------------')
#로또 번호를 생성하고 텍스트 파일에 출력해보기

import random

uri = 'E:/pythonTxt/'
def writeLotto(nums): #nums 보너스 번호를 포함한 전체 숫자 리스트
    for idx, num in enumerate(nums): #num은 nums 리스트를 돌고 있는 변수
        with open(uri + 'lotto.txt', 'a') as f:
            #len-1 : 리스트의 가장 마지막 번호
            #len-2 : 리스트의 가장 마지막에서 두번째번호(로또로 치면 보너스번호 제외한 가장 끝 번호)
            if idx < len(nums) -2 : #보너스 및 마지막 번호를 제외한 의미
                f.write(str(num) + ',')
            elif idx == len(nums)-2: #보너스 번호 제외한 가장 마지막 번호 의미
                f.write(str(num))
            elif idx == len(nums)-1:
                f.write('\n')
                f.write('bonus: ' + str(num))
                f.write('\n')

rNums = random.sample(range(1,46), 7)
print(f'rNums:{rNums}')

#실행문에 랜덤숫자 리스트 넣어주기
writeLotto(rNums)



