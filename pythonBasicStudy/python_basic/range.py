# range(시작, 끝, 단계) -> 단계란? 얼마나 띄어서 사용할 것인가
range(9) #0부터 8까지 1씩 증가(시작이 0으로 시작할 때 사용)

start = int(input('반복의 시작 번호 : '))
end = int(input('반복의 끝 번호 : '))

for i in range(start,end+1):
    print(i)