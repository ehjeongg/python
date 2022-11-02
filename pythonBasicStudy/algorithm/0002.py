# 보초법이란?
# 리스트의 가장 마지막에 찾는 값을 넣어서 '종료조건'을 실행하는 것을 제거하여 조금 더 빠르게 검색할 수 있는 방법

# Q. 리스트에서 가장 앞에 있는 숫자 7을 검색하고 인덱스 출력
nums = [4,7,10,2,4,7,0,2,7,3,9]

search = int(input('검색할 숫자 입력'))
searchIndex = -1 #인덱스의 결과로 나오는 것이라 -1로 초기화 시켜줌

nums.append(search) #보초법을 사용하기 위함

n=0 #while문을 사용하기 위함

while True:
    if nums[n] == search:
        if n!= len(nums)-1: #보초법을 사용했기 때문에 마지막 인덱스(리스트 길이)는 제외시킴
            searchIndex=n
            break
    n+=1
print(f'인덱스 번호는: {searchIndex}')
print(f'몇번째에 있는지 : {searchIndex-1}')

if search < 0: #입력한 값의 인덱스를 찾지 못한 경우
    print('입력 결과가 없습니다.')
else:
    print(f'searchIndex : {searchIndex}')