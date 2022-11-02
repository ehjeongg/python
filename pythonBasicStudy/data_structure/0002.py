misScore = 60
scores=[['a', 58],
        ['b',35],
        ['c', 76],
        ['d',89]]

for i in scores:
    if i[1] < misScore:
        print('과락:{}, 점수:{}'.format(i[0], i[1])) #인덱스를 이용하는 방법

print('---------------------------------------------------------------------')

for subject, score in scores:
    if score < misScore:
        print('과락:{}, 점수:{}'.format(subject, score)) #인덱스를 이용하는 방법

print('---------------------------------------------------------------------')

for subject, score in scores:
    if score >= misScore: continue #minScore보다 크면 continue 계속 지나간다(아래 내용 무시하고)
    #위에 if 조건에 맞지 않는 경우 아래 코드에 맞게 실행한다
    print('과락:{}, 점수:{}'.format(subject, score)) #인덱스를 이용하는 방법

print('---------------------------------------------------------------------')

for subject, score in scores:
    if score >= misScore: #해당 조건에 맞는경우 아래 조건을 실행한다
        print('과락:{}, 점수:{}'.format(subject, score))  # 인덱스를 이용하는 방법