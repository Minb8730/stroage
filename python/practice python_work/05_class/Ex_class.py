'''
객체 지향 프로그래밍 (OOP : Object Oriented Programming)
- class 로 부터 만들어진 객체들의 상호관계를 이용해서 하나의 프로그램을 만드는 것을 말함.

class
- 객체를 만들기 위한 하나의 틀
- 속성(변수)과 기능(메서드)으로 구성되어 있습니다.

객체
- class로 부터 만들어진 결과물

class 구성
- class 클래스이름 :
        attr =10
        def method():

- class 명은 대문자로 시작
  변수(데이터) : 속성 값
  메서드(함수) : 기능 구현

'''

class Unit:
    # 속성
    hp = 500
    atk = 30
    defs = 100

    # 메서드
    def attack(self):
        print(" - 공격 - ")

    def defense(self):
        print(" - 방어 - ")



'''
객체 생성
- 변수 = 클래스명()
'''
# userA = Unit()
# userA.attack()
# userA.defense()


'''
생성자
- 생성자는 객체가 생성 될 때 클래스의 멤버변수를 초기화하거나,
  객체 생성과 동시에 해야할 내용을 기술
- 객체를 만들 때 자동으로 실행 됨
- 별도로 정의하지 않으면 기본 생성자가 자동으로 실행
'''

# class Unit:

#     def __init__(self, hp = 100, atk = 10, defs = 10 ):
#         self.hp = hp
#         self.atk = atk
#         self.defs = defs

#     def info(self):
#         print("HP : {} - ATK : {} - DEF : {}".format(self.hp, self.atk, self.defs))
    
# unitA = Unit(100, 100, 100)
# unitA.info()

# unitB = Unit(50, 50)
# unitB.info()


'''
self
- 객체 자신을 뜻합니다.
- 메서드의 첫번째 매개변수로 사용
- 호출시에 객체 자신이 전달되기 때문에 self 이름을 사용
'''

# class Unit:

#     def __init__(self, hp = 100, atk = 10, defs = 10 ):
#         self.hp = hp
#         self.atk = atk
#         self.defs = defs
    
#     def atkUp(self, up):
#         self.atk += up
#         print("ATK UP :", self.atk)

#     def info(self):
#         print("HP : {} - ATK : {} - DEF : {}".format(self.hp, self.atk, self.defs))

# unitC = Unit()
# unitC.info()
# unitC.atkUp(50)
# unitC.info()

'''
accessor
- class의 멤버는 모두 공개되어 어디에서나 접근이 가능하지만,
  class 멤버를 내부에서만 사용 할 수 있게 설정 할 수도 있습니다.
- getter 메서드 : 멤버필드 값을 읽을 때 사용
  setter 메서드 : 멤버필드 값을 수정 할 때 사용
'''

class Person:

    def __init__(self, name ="none", age = 0):
        self.name = name
        self.__age = age # 외부에서 직접 사용하지 못하고 함수 내에서만 수정이 가능하도록 '__' 를 붙인다.

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("0 이상의 값을 사용하세요.")

    def info(self):
        print("이름 : {} - 나이 : {}".format(self.name, self.__age))

manA = Person("manA", 20)
manA.info()
# man.age = -21 # 외부에서 사용하는 경우
print("나이 :", manA.getAge())
manA.info()
manA.setAge(-21)