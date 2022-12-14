# 선수의 원본 점수를 이용해서 평균을 출력, 최고/최저값을 제외한 평균을 출력하는 프로그램 만들기
plaOriSco = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
plaCopSco = plaOriSco.copy()

plaOriSco.sort()

plaCopSco.sort()
plaCopSco.pop(0)
plaCopSco.pop()

print(f'plaOriSco: {plaOriSco}')
print(f'plaCopSco: {plaCopSco}')


oriTot = round(sum(plaOriSco), 2)
oriAvg = round(oriTot / len(plaOriSco), 2)
print(f'Original Total: {oriTot}')
print(f'Original Average: {oriAvg}')

copTot = round(sum(plaCopSco), 2)
copAvg = round(oriTot / len(plaCopSco), 2)
print(f'Copy Total: {copTot}')
print(f'Copy Average: {copAvg}')


print(f'oriAvg - copAvg: {oriAvg - copAvg}')



