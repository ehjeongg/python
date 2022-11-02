print('3*5=', end='')#end함수는 자동으로 개행이 되는 것을 막아줌
print(3*5)
print(3*5)
print('') #print() 함수는 자동으로 개행이 됨
print('3*5=', end='여기에 들어감')
print(3*5)

#포맷문자열을 이용한 데이터 출력
name='이름이란'
age=2

print(f'User name: {name} \n age : {age}') #f'{변수명}' #개행할 때 \n 사용

print(f'User name: {name} \t age : {age}') #f'{변수명}' #\t는 탭

food = 'pizza'
agee = 27
print('나는 {0}를 좋아해, 나이는 {1}이고, {0}집 차릴꺼야'.format(food, agee))

#format함수 사용하는형식
#print(''.format(var1, var2))

# %s 문자열 %f 실수 %d 정수
# %.3f : 소수점 세번째까지 노출함
print('name 형식을 정하는 프린트 포맷 : %s' % name )




