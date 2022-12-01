# #고도60m 올라갈때마다 기온이 0.8도 내려감, 현재 지면 온도 29도
#고도 올라갈때마다 그 고도의 기온 구하기
base = 29
step = 60
height = int(input('고도를 입력하세요')) #연산을 하기 위한 형변환

currentTemp = base - (height // step * 0.8) #고도를 step으로 나눈 몫에 0.8을 곱해줌

if  height % step != 0: #60을 나눈 나머지가 있을 때 그것 또한 -0.8 온도임을 체크
    currentTemp -= 0.8

print('지면온도:{}'.format(base))
print('고도 {}m의 기온:{}'.format(height, currentTemp))

#197개의 빵과 152개의 우유를 17명한테 동일하게 나누주고 남은 개수 구하기
bread = 197
milk = 152
student = 17
breadDiv = bread //17
milkDiv = milk//17

breSpa=bread % student
milSpa=milk % student
print('나눈 준 빵의 양:{}'.format(breadDiv))
print('나눈 준 우유의 양:{}'.format(milkDiv))

print('남은 빵 : {} 남은 우유 : {}'.format(breSpa,  milSpa))


#길이 입력하면 인치로 환산하는 프로그램 (1mm= 0.039inch)

inch= 0.039
length=int(input('길이입력'))
inchLength=inch * length

print('{}mm는 {}inch이다.'.format(length, inchLength))