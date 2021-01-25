'''
나이를 사용해서 버스요금이 얼마인지를 알려주는 코드를 작성
-어린이(8세 미만) 450원, 학생 ( 8~ 19 ) 720원, 일반 (20 이상) 1250원

'''


# generation = ("")
# money = ""

# age = int(input())
# if age < 8 :
#     generation = "어린이"
#     money = 450
# elif age < 19 :
#     generation = "학생"
#     money = 720
# elif age > 19 :
#     generation = "일반"
#     money = 1250

# print("{}입니다. 요금은 {} 원 입니다.".format(generation, money))

'''#실패함 ㅠㅠ

알파벳이 소문자이면 대문자로, 대문자이면 소문자로 변환하는 코드를 작성하세요
'''
'''
switch = input("알파벳 입력 : ")
print("switch :", switch)
ach = ord(switch)

dataCheck = True #알파벳 확인 - True : 0 , False : X

if ach >= ord('A') and ach <= ord('Z')  :
    ach = chr(ach + 32)
elif ach >= ord('a') and ach <= ord('z') :
    ach= chr(ach -32)
else :
    print('알파벳이 아닙니다.')

'''


'''
차량 속도에 따라 벌금, 벌점을 구하는 코드를 작성하세요
-속도               벌점 벌금
0    초과 ~ 100 이하  0    0
100  초과 ~ 120 이하  0    3
120  초과 ~ 140 이하  15   6
140  초과 ~ 160 이하  30   9
160  초과 ~           60   12
'''

'''
car_speed = int(input())
disadvantage = ""
charge = ""

if car_speed <= 100 :
    disadvantage = 0
    charge = 0
elif 100 <= car_speed <= 120 :
    disadvantage = 0
    charge = 3
elif 120 <= car_speed <= 140 :
    disadvantage = 15
    charge = 6
elif 140 <= car_speed <= 160 :
    disadvantage = 30
    charge = 9
else :
    disadvantage = 60
    charge = 12

print("차량 속도 : {} km\t벌점 : {}점\t벌금 : {}만원".format(car_speed, disadvantage, charge))
'''

'''
몸무게 (kg), 키(cm)를 사용해서 체질량지수(BMI) 값을 계산하여 몸상태를 알려주는 코드를 작성
-    BMI  =  몸무게(kg)  /  키(m) * 키(m)

bmi                 몸상태
0       ~18.4       저체중
18.5    ~22.9       정상
23.0    ~24.9       과체중 
25.0    ~29.9       비만

'''



weight = float(input("몸무게 입력 :"))
height = float(input("키 입력 :"))
mheight = height / 100
BMI = weight / (mheight*mheight)
print("{:.1f}".format(BMI)) #소수점 구하는 방법

body = ""

if BMI <= 18.4:
    body = "저체중"
elif 18.5 <= BMI <= 22.9:
    body = "정상"
elif 23.0 <= BMI <= 24.9:
    body = "과체중"
elif 25.0 <= BMI <= 29.9:
    body = "비만"

print("현재의 몸무게 : {0}kg,\n현재의 키 : {1}cm\nBMI : {2:.1f}\n당신은 현재 {3} 입니다. ".format(weight, height, BMI, body))
