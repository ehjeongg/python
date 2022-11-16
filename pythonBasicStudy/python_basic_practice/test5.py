import datetime

print(datetime.date.today()) #날짜만 출력
print(datetime.datetime.today()) #시간까지 출력
print(datetime.datetime.now()) #시간까지 출력

print('-' * 100)

today = datetime.date.today()
age = input('나이입력')
if age.isdigit():
    after = 100-int(age)
    bb = today.year + after
    print('{}년 {}년 후에 100살'.format(bb, after))
else:
    print('잘못입력')