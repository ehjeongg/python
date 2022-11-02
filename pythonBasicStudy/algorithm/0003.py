#리스트에서 숫자 7을 모두 검색하고 각각의 위치와 검색 개수를 출력(검색개수는 n+나 len 이용하기)

nums = [4,7,10,2,4,7,0,2,7,3,9]
search = int(input('인덱스의 위치와 입력한 숫자의 개수를 알고싶으면 원하는 값을 넣어라'))
resultIndex = [] #7이 있는 인덱스 결과만 넣을 새로운 리스트 초기화
nums.append(search)
n=0 #while문을 사용하기 위함
while True:
    if nums[n] == search:
        if n != len(nums) -1: #맨 마지막에 있는 것은 아니여야 한다
            resultIndex.append(n)
        else:
            break

    n+=1  #무한 반복에 빠지지 않도록 nums[n] 사이에서만 반복될 수 있도록 함

print(f'7의 각 위치 : {resultIndex}')
print(f'7의 개수 : {len(resultIndex)}')