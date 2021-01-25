#251
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.

'''
클래스 : 붕어빵 틀과 같은것, 객체나 인스턴스의 설계도
객체 object 인스턴스: 클래스로부터 만들어진 
클래스를 강조하고 싶지 않을때는 객체
강조하고 싶을때 인스턴스

개발자가 만드는 클래스명은 대문자로 시작
클래스 안의 함수는 메소드라고 부른다.
클래스도 타입의 객체이다.
'''

#252
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
# class Human:
#     pass

#253
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.

# areum = Human()

#254
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.

# >>> areum = Human()
# 응애응애

# class Human:
#     def __init__(self):  # 생성자(__init__) -> 객체를 생성한 다음*에 자동으로 함수를 호출한다. / self : 생성된 객체를 바인딩 즉 생성된 객체를 의미 
#         print("응애응애")

# areum = Human()
# print(areum)
# print()


#255
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")

# class Human:
#     def __init__(self):
#         print("응애응애")

#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
        
# areum = Human("아름", 25, "여자")
# print(areum.name)
print()


#256
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예

# >>> areum.age
# 25

# areum = Human("조아름", 25, "여자")
# print(areum.name, areum.age, areum.sex)



#257
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자


# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
    
#     def who(self):
#         print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.sex))
    
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
    

# areum = Human("조아름", 25, "여자")
# areum.who()
# print()
# Human.who(areum)


#258
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")


# areum = Human("불명", "미상", "모름")
# areum.who()  #->자동으로 인터프리터가  # Human.who(areum) 로 해석

# areum.setInfo("아름", 25, "여자")
# areum.who()      # Human.who(areum)


#259
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라



class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.sex))
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def __del__(self):  # 소멸자
        print("나의 죽음을 알리지마라")


areum = Human("아름", 25, "여자")
areum.who()


#260
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

# class OMG : 
#     def print() :
#         print("Oh my god")

# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()

# TypeError: print() takes 0 positional arguments but 1 was given

'''
mystock = OMG()
mystock.print() -> OMG.print(mystock)  -> def print() 는 인자를 받지 않는데 mystock이 들어가기 때문에
Error 출력이 되지 않게 하려면 def print(self): 로 해주어야 한다.
'''





