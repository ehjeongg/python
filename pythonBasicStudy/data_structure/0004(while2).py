students = [[1,18], [2,19], [3,23], [4,21], [5,50]]
#사용할 변수들은 초기화 해야함
n=0
sum=0
avg=0
while n < len(students):
    classNo = students[n][0] # class라는 변수는 예약어라서 사용할 수 없음
    count = students[n][1]
    sum +=count
    n+=1
    avg = sum / len(students)

print(sum)
print(len(students))
print('전체 학생수 : {}'.format(sum))
print('전체 평균 학생수:{}'.format(avg))

# while True:
#    n<len(students)
#    n+=1
#    sumStudent = sum(students[n][1])
#    print(sumStudent)
#    avgStudent = int(sumStudent/len(students))
#    print('학급별 학생수 : {}반, {}명'.format(students[n][0], students[n][1]))
#    print('전체 학생수 : {}'.format(sumStudent))
#    print('학급 평균 학생수 : {}'.format(avgStudent))
#    -> 오류 난 풀이

