#중간고사 클래스와 기말고사 클래스의 상속관계 만들고 각각의 점수 초기화
#총점 및 평균을 반환하는 기능도 만들기

class MidExam:
    def __init__(self, s1, s2, s3 ):
        print('[MidExam] __init__() ')

        self.midKor = s1
        self.midMath = s2
        self.midEng = s3

    def printMid(self):

        print(f'국어 : { self.midKor}')
        print(f'수학 : {self.midMath}')
        print(f'영어 : {self.midEng}')

class FinalExam(MidExam): #중간고사 클래스 상속받기
    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[FinalExam] __init__() ')

        super().__init__(s1, s2, s3)

        self.finalKor = s4
        self.finalMath = s5
        self.finalEng = s6
