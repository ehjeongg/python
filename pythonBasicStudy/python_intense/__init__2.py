class P_class:
    def __init__(self, pnum1, pnum2):
        print('[P_class] __init__() called!')

        self.pnum1 = pnum1
        self.pnum2 = pnum2


class C_class:
    def __init__(self, cnum1, cnum2):
        print('[C_class] __init__() called!')
        self.cnum1 = cnum1
        self.cnum2 = cnum2

    # # 만약 P_class의 속성들도 C_class이 쓰고 싶다면(강제 호출)
    #     P_class.__init__(self, cnum1, cnum2)
    #     #=> P_class의 init을 강제 호출하여 현재 위치해 있는 C_class의 매개변수를 추가
    #     #결과 : p / c 두 개의 클래스를 모두 불러오게됨

    # # 만약 P_class의 속성들도 C_class이 쓰고 싶다면(super() 사용)
    # 상위 클래스로 가서 init 호출하고 매개변수로 cnum1, cnum2를 초기화 하라는 뜻
        super().__init__(cnum1, cnum2) #super()를 사용하면 self를 안써줘도 됨

CLS = C_class(10,20) #[C_class] __init__() called! C_class의 init 메소드가 호출 된 것을 알 수 있음


#기능은 상속하면 다 쓸 수 있지만, 속성은 __init__ 메소드가 호출이 되고, 속성이 초기화한 후에 사용할 수 있음

