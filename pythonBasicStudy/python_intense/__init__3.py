#중간고사 클래스와 기말고사 클래스의 상속관계 만들고 각각의 점수 초기화
#총점 및 평균을 반환하는 기능도 만들기

class MidExam:
    def __init__(self, s1, s2, s3 ):
        print('[MidExam] __init__() ')

        self.midKor = s1
        self.midMath = s2
        self.midEng = s3

    def print(self):

        print(f'중간국어 : {self.midKor}')
        print(f'중간수학 : {self.midMath}')
        print(f'중간영어 : {self.midEng}')

class FinalExam(MidExam): #중간고사 클래스 상속받기
    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[FinalExam] __init__() ')

        super().__init__(s1, s2, s3) #위에 작성된 부모클래스에서의 매개변수를 상속받음

        self.finalKor = s4
        self.finalMath = s5
        self.finalEng = s6

    def print(self):
        #super().print() -> 상속받은 것도 같이 출력하겠다는 의미
        super().print()
        print(f'기말국어 : {self.finalKor}')
        print(f'기말수학 : {self.finalMath}')
        print(f'기말영어 : {self.finalEng}')

    def totalScore(self):
        total = self.midKor +  self.midMath + self.midEng
        total += self.finalKor + self.finalMath +  self.finalEng

        return total

    def avgScore(self):
        return self.totalScore() / 6

        # avg = self.totalScore() / 6
        # return avg

exam = FinalExam(13,24,54,35,24,46)
exam.print()

#전체 중간/기말 점수가 나와야함 -> 여기서 모든 점수가 나오지 않는 이유 찾기
#자식 클래스 print 함수에서 super().print라는 상속받은 클래스를 출력하는 코드가 없었음

print(f'총점 : {exam.totalScore()}')
print(f'평균 : {round(exam.avgScore(), 1)}')

