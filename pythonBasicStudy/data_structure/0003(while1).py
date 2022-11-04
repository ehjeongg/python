#while문을 이용한 다양한 조회(아래 3가지 방법)
chrs = [ 'a', 'b', 'c', 'd', 'e']

n=0
while n < len(chrs):
    print(chrs[n])
    n+=1

n=0
flag = True
while flag:
    print(chrs[n])
    n+=1

    if n==len(chrs):
        flag = False # 무한 반복 방지

n=0
while True:
    print(chrs[n])
    n+=1

    if n==len(chrs):
        break #무한 반복을 막기 위해서임
