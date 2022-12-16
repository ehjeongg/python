#writelines() : 반복가능한 자료형의 데이터를 파일에 쓰자
#=> 리스트(list) 또는 튜플 데이터를 파일에 쓰기 위한 함수

#                      아래와 같은 반복문(->반복 가능한 객체)을

# languages = ['c/c++', 'java', 'c#', 'python', 'javascript']
#
# uri = 'C:/pythonTxt/'
# for item in languages:
#     with open(uri + 'languages.txt', 'a') as f:
#         f.write(item)
#         f.write('\n')



#         writelines()를 이용하면 아래와 같이 표현할 수 있음

languages = ('c/c++', 'java', 'c#', 'python', 'javascript')

uri = 'E:/pythonTxt/'
with open(uri + 'languages.txt', 'a') as f:
    # f.writelines(languages)
    f.writelines(item + '\n' for item in languages)

print('실습--------------------------------------------------------------------')

scoreDic = {'kor': 85, 'eng': 90, 'mat': 92, 'sci': 79, 'his': 82}
uri = 'E:/pythonTxt/'

with open(uri + 'score.txt', 'a') as file:
    # file.writelines(s + '\n' for s in scoreDic)
    print(scoreDic, file = file) #리스트 형태 그대로 출력됨

