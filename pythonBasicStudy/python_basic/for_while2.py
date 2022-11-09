#1부터 시작해서 7의 배수의 합이 50이상인 최초의 정수 출력(조건에 의해서 반복이 돌아야함)
hap = 0
maxInt = 0
n=1
while n <= 100 and hap <= 50:
    n+=1
    if n%7==0:
        hap +=n
        maxInt = n

    print('n : {}'.format(n))

print('7의 배수의 합이 50이상인 최초의 정수: {}'.format(maxInt))
print('n : {}'.format(n))

print('-'*60)

# 자동차 바퀴가 한번 구를 때마다 0.15mm씩 마모된다
# 현재의 바퀴 두께가 30mm이고 최소 운행 가능 바퀴두께가 20mm라고 할 때 앞으로 구를 수 있는 횟수

currentThick = 30
attack = 0.15
count=0
while currentThick >= 20:
    currentThick -=attack
    count += 1
res = count-1
#1을 빼는 이유? 만약 20.2에서 0.15를 뺀 이후에 count+1을 하고나서 while문을 빠져나올 것을 생각
#count할 때 한번 더 더해질 수 있는 점을 고려
print('앞으로 구를 수 있는 횟수 : {} '.format(res))

