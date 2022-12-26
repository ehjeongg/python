#약수 : 어떤 수를 나누어 떨어지게 하는 수
#소수 : 1과 자신만을 약수로 가지는 수(단, 1은 제외)
#소수를 구하는 방법? ->
#실습 : 1~30까지의 숫자 중 5로 나눈 몫과 나머지가 모두 소수인 숫자들을 찾아보라

def findNumber(n):
    list =[]
    for i in range(2,30):
        mok = i //5
        rest = i % 5

        for j in range(2,30):
            if j % mok ==0:
                return False
        return list.append(i)

        for j in range(2,30):
            if j % rest ==0:
                return False
        return list.append(i)
print(list)






