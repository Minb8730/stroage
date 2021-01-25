#281
# 다음 코드가 동작하도록 차 클래스를 정의하세요.

# car = 차(2, 1000)
# car.바퀴
# 2
# car.가격
# 1000

# class 차:
#     def __init__(self, wheel,price):
#         self.wheel = wheel
#         self.price = price

# car = 차(2, 1000)
# print(car.wheel)
# print(car.price)


#282
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.

# class 자전차(차):
#     pass



#283
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.

# bicycle = 자전차(2, 100)
# bicycle.가격
# 100



# class 차:
#     def __init__(self, wheel,price):
#         self.wheel = wheel
#         self.price = price


# class 자전차(차):
#     pass
# bicycle = 자전차(2, 100)
# print(bicycle.price )


#284

# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.

# bicycle = 자전차(2, 100, "시마노")
# bicycle.구동계
# 시마노


# class 차:
#     def __init__(self, wheel,price):
#         self.wheel = wheel
#         self.price = price


# class 자전차(차):
#     def __init__(self, wheel, price, 구동계):
#         super().__init__(wheel,price)   # 차.__init__(wheel, price)
#         self.구동계 = 구동계


# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.구동계)




#285
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.

# car = 자동차(4, 1000)
# car.정보()
# 바퀴수 4
# 가격 1000




# class 차:
#     def __init__(self, wheel,price):
#         self.wheel = wheel
#         self.price = price

# class 자동차(차):
#     def __init__(self, wheel, price):
#         super().__init__(wheel, price)

#     def 정보(self):
#         print("바퀴수 ", self.wheel)
#         print("가격 ", self.price)


# car = 자동차(4, 1000)
# car.정보()



#286


# 다음 코드가 동작하도록 자전차 클래스를 수정하세요.

# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()
# 바퀴수 2
# 가격 100




# class 차:
#     def __init__(self, wheel,price):
#         self.wheel = wheel
#         self.price = price

#     def 정보(self):
#         print("바퀴수 ", self.wheel)
#         print("가격 ", self.price)


# class 자동차(차):
#     def __init__(self, wheel, price):
#         super().__init__(wheel, price)

# class 자전차(차):
#     def __init__(self, wheel, price, 구동계):
#         super().__init__(wheel,price)   # 차.__init__(wheel, price)
#         self.구동계 = 구동계
    
    

# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()


#287
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.

# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()
# 바퀴수 2
# 가격 100
# 구동계 시마노

class 차:
    def __init__(self, wheel,price):
        self.wheel = wheel
        self.price = price

    def 정보(self):
        print("바퀴수 ", self.wheel)
        print("가격 ", self.price)

class 자동차(차):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

class 자전차(차):
    def __init__(self, wheel, price, 구동계):
        super().__init__(wheel,price)   # 차.__init__(wheel, price)
        self.구동계 = 구동계

    def 정보(self):
        super().정보()
        print("구동계 ",self.구동계)    

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()



#288
# 다음 코드의 실행 결과를 예상해보세요.

# class 부모:
#   def 호출(self):
#     print("부모호출")

# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
# 나 = 자식()
# 나.호출()

'''

자식호출

'''


#289
# 다음 코드의 실행 결과를 예상해보세요.

# class 부모:
#   def __init__(self):
#     print("부모생성")

# class 자식(부모):
#   def __init__(self):
#     print("자식생성")

# 나 = 자식()
'''
자식생성
'''


#290
# 다음 코드의 실행 결과를 예상해보세요.

# class 부모:
#   def __init__(self):
#     print("부모생성")

# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()

# 나 = 자식()

'''
자식생성
부모생성
'''








