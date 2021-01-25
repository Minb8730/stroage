

# Ex04-Quiz_if-elif.py

'''
나이를 사용해서 버스요금이 얼마인지를 알려주는 코드를 작성하세요
- 어린이(8세 미만) 450, 학생( 8 ~ 19 ) 720, 일반(20 이상) 1250
'''
# age = int(input("나이 입력 > "))
# print()

# fare = 0
# if age < 8:
#     fare = 450
# elif age < 20:
#     fare = 720
# else:
#     fare = 1250
# print("요금 : {} 원".format(fare))


'''
알파벳이 소문자이면 대문자로, 대문자이면 소문자로 변환하는 코드를 작성하세요
'''
# ch = input("알파벳 입력 > ")
# print()
# print("ch :", ch)
# ach = ord(ch)

# dataCheck = True # 알파벳 확인 - True : O, False : X
# if ach >= ord('A') and ach <= ord('Z'):
#     ach = chr(ach + 32)
# elif ach >= ord('a') and ach <= ord('z'):
#     ach = chr(ach - 32)
# else:
#     print('알파벳이 아니에요..')
#     dataCheck = False
# if dataCheck:
#     print("{} 변환 문자 : {}".format(ch, ach))



'''
차량 속도에 따라 벌금, 벌점을 구하는 코드를 작성하세요
- 속도                벌점   벌금
  0   초과 ~ 100 이하   0      0
  100 초과 ~ 120 이하   0      3
  120 초과 ~ 140 이하  15      6
  140 초과 ~ 160 이하  30      9
  160 초과 ~          60      12
'''
# speed = int(input("속도 입력 > "))
# print()

# penalty = 0  # 벌점
# money = 0    # 벌금
# if speed > 160:
#     penalty = 60
#     money = 12
# elif speed > 140:
#     penalty = 30
#     money = 9
# elif speed > 120:
#     penalty = 15
#     money = 6
# elif speed > 100:
#     penalty = 0
#     money = 3

# print("속도 : {} km".format(speed))
# print("벌점 : {} - 벌금 : {} 만원".format(penalty, money))


'''
몸무게(kg), 키(cm)를 사용해서 체질량지수(BMI) 값을 계산하여 몸상태를 알려주는 코드를 작성하세요
-            몸무게(kg)
  BMI = ---------------------
         키( m ) * 키( m )
  bmi                 몸상태
  0     ~ 18.4        저체중
  18.5  ~ 22.9        정상
  23.0  ~ 24.9        과체중
  25.0  ~ 29.9        비만
  30.0  ~             고도비만  
'''
weight = float(input("몸무게 입력 > "))
height = float(input("키 입력 > "))
print()

mHeight = height / 100
bmi = weight / (mHeight * mHeight)

userBody = "고도비만"
if bmi < 18.5:
    userBody = "저체중"
elif bmi < 23.0:
    userBody = "정상"
elif bmi < 25.0:
    userBody = "과체중"
elif bmi < 30.0:
    userBody = "비만"

print("몸무게 : {} kg".format(weight))
print("키    : {:.1f}cm".format(height))
print("BMI   : {:.1f}".format(bmi))
print("몸상태 : {}".format(userBody))







































