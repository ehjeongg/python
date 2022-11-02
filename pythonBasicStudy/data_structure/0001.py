# 지료가 어떤 구조로 형성되어 있는지
# 리스트는 요소 변경 가능하지만, 튜플은 변경 불가

# set데이터는 중복을 제거함

# 리스트는 숫자, 문자, 논리형 등 모든 기본 데이터를 같이 저장할 수 있음

# 리스트 변수는 보통 변수명s 붙이는게 관례

#len()과 반복문을 이요하면 리스트의 아이템(요소)조회가능
students =['a', '1', 2, True, 'false']


for i in range(len(students)):
    print(i) #인덱스의 번호를 출력함
    #같은 라인에 있으면, 아래 print 함수도 반복문을 돌게 됨
print(students[3]) #인덱스 3번에 있는 아이템을 꺼내옴

lists = [[2,3], [4,5], [6,7], [8,9]]
# for i in range(len(lists)):
#     print('1차원:{}, 2차원:{}'.format(lists[i][0], lists[i][1])    )
#위아래 같은 결과를 나타내는 for문
for i, j in lists:
    print('1: {}, 2:{}'.format(i,j))
#가독성을 위해서라도 변수를 사용하는 것이 낫다


