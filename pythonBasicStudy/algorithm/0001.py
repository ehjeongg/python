#algorithm 문제를 풀기위한 공식과 절차

datas = [1,2,3,4,5,6,7,8]
print(f'datas: {datas}')

searchData = int(input('찾는값 입력'))
searchIndex = -1
n=0
while True:
    if n==len(datas):
        searchIndex = -1
        print('찾는 값이 없습니다')
        break
    elif datas[n] == searchData:
        searchIndex = n
        break

    n+=1

print(searchIndex)

#보초법 : 마지막 인덱스에 찾으려는 값을 추가하는 찾는 과정을 간략화한다.