#중첩 반복문 : 반복문 안에 또 다른 반복문을 선언

for i in range(1,10):
    for j in range(i):
        print('*', end='')
    print()

print('')
for k in range(10,0,-1):
    for s in range(k):
        print('*', end='')
    print()

#구구단 만들어보기
for q in range(1,10):
    for w in range (2,10):
        result = q * w
        print('{} * {} = {}\t'.format(w, q, result), end='') #개행하지 말라고 end=''를 추가
    print() #공백이 있는 줄을 주고 다시 반복문을 실행