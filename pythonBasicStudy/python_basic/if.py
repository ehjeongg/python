#if ~ elif 문(다자택일 조건문) : 여러가지 조건식 결과에 따라 실행문 결정
#마지막 else는 생략가능

print('계절: 봄, 여름, 가을, 겨울')
user = str(input('계절입력')) #형변환(casting) 할 때 파이썬은 str을 사용

if user == '봄':
    print('{} : {}'.format('봄', 'spring'))
elif user == '여름':
    print('{} : {}'.format('여름', 'summer'))
elif user=='가을':
    print(f'입력값 : {user}, 영어: atume')
else:
    print('잘못입력')

#다자택일 사용시 주의할 점 -> 조건식 순서가 중요하다
#순서를 신경쓰기 싫다고 하면 조건의 범위를 정확하게

