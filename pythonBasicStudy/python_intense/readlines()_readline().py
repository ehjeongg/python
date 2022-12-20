# readlines() : 파일의 모든 데이터를 읽어서 리스트 형태로 반환(눈에 보이지 않는 개행표시까지 읽어옴)
# readline() : 한 줄씩 읽어서 문자열로 반환함

# uri = 'E/pythonTxt/'
# with open(uri + 'lans.txt', 'r') as f:
#     lanList = f.readlines()
# print(f'lanList : {lanList}')
# print(f'lanListType : {type(lanList)}')
#
#lans.txt 파일이 존재하지 않는다고 오류남

# #실습 : 파일에 저장된 과목별 점수를 파이썬에서 읽어, 딕셔너리에 저장하는 코드를 작성

scoreDic={} #딕셔너리 자료형

uri = 'E/pythonTxt/'
with open(uri + 'scores.txt', 'r') as f:
    line = f.readline()

    #while 조건 : 해당 조건에 True일 경우
    while line != '': #해당 라인이 공백이 아니라면(과목과 점수가 있는 동안에 돌아가는 반복문)
        # 해당 기호 기준으로 모든 요소들을 리스트 형태로 반환함
        tempList = line.split(':') # split은 구분자를 이용해서 과목명과 점수를 따로 분리해서 리스트에 담아줌
        scoreDic[tempList[0]] = int(tempList[1].strip('\n')) #개행을 제거 하기
        # 과목, 점수로 쪼개진 리스트 첫번째 과목을 담음
        # 리스트에서 두번째인 점수는 int로 형변환을 하고 strip

        line = f.readlines()

print(f'scoreDic: {scoreDic}')

# 오류남 -> No such file or directory: 'E/pythonTxt/scores.txt'

