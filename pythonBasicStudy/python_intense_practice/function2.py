#파이썬 중급 41강


# #시간 / 거리 입력시 이동거리 출력
# #거리 / 속력 입력시 이동시간 출력 하는 프로그램
# -> 프로그래밍 하기전에 기능 부터 만들고 나중에 입력받기

#h m s

def distance(h, m, s): #시간, 분, 속력입력(거리 = 속력 x 시간)
    return s * (h + m/60) #속력 x 시간  // 분은 60으로 나눠서 시간과 단위를 맞춰줌

def gettime(s, d):
    time = d / s #시간은 거리 % 속력
    print(f'time : {time}')
    h = int(time) #시간
    m = int((time - h ) * 100 * 60 /100) #어떤 의미인지
    return [h,m] #리스트 형태로 뽑아서 어디에 쓰려구


#강사 예시 코드
print('-------------------------------------------------------------------------------------------')

# 거리(km) = 속도(km/h) * 시간(h)
def getDistance(speed, hour, minute):
    distance = speed * (hour + (minute / 60))

    return distance


def getTime(speed, distance):
    time = distance / speed
    print(f'time: {time}')
    h = int(time)
    m = int((time - h) * 100 * 60 / 100)
    # m = convertFloatToMinute(time - h)

    return [h, m]


def convertFloatToMinute(f): #float으로 받은것을 minute으로 변경하는 이유는?
    return int(f * 100 * 60 / 100)


print('-' * 60)
s = float(input('속도(km/h) 입력: '))
h = float(input('시간(h) 입력: '))
m = float(input('시간(m) 입력: '))
d = getDistance(s, h, m)
print(f'{s}(km/h)속도로 {h}(h)시간 {m}(m)분 동안 이동한 거리: {d}(km)')
print('-' * 60)



print('-' * 60)
s = float(input('속도(km/h) 입력: '))
d = float(input('거리(km) 입력: '))
t = getTime(s, d)
print(f'{s}(km/h) 속도로 {d}(km) 이동한 시간: {t[0]}(h)시간 {t[1]}(m)분')
print('-' * 60)