

# Ex06-Quiz_while.py

'''
입력에 0이 들어올 때 까지의 합을 구하는 코드를 작성하세요
'''
# sum = 0    # 합
# data = 1   # 입력 값
# while data != 0:
#     data = int(input("숫자 입력 > "))
#     sum += data
# print("합 :", sum)


'''
1 이상의 숫자 3개의 합을 구하는 코드를 작성하세요
- 3개의 값은 모두 저장하지 않아도 되고, -(마이너스) 값은 사용 할 수 없습니다
'''
# count = 1    # 입력 횟수
# value = 0    # 입력 값
# total = 0    # 합

# while count <= 3:
#     value = int(input("{}번째 입력 > ".format(count)))
#     if value >= 0:
#         total += value
#         count += 1
# print("입력 값의 합 :", total)



'''
이름, 나이, 성별을 입력받아서 출력하는 코드를 작성하세요
- 나이는 0 ~ 130 사이만 가능합니다
- 성별은 남성, 여성만 가능합니다
'''
# userName = ""
# nameCheck = True
# while nameCheck:
#     userName = input("이름 입력 > ")
#     if len(userName) < 11:
#         nameCheck = False
# print()

# userAge = 0
# ageCheck = True
# while ageCheck:
#     userAge = int(input("나이 입력 > "))
#     if userAge >= 0 and userAge <= 130:
#         ageCheck = False
# print()

# userGender = ""
# genderCheck = False
# while not genderCheck:
#     userGender = input("성별 입력 > ")
#     if userGender == "남성" or userGender == "여성":
#         genderCheck = True
# print()

# print("--- 입 력 정 보 ---")
# print("이름 :", userName)
# print("나이 :", userAge)
# print("성별 :", userGender)



'''
치즈 10Box가 있는 창고에 암수 1쌍의 쥐가 살고 있습니다
쥐 한마리가 하루에 먹을 수 있는 치즈의 양은 20g 이고, 치즈를 먹은 10일마다 쥐의 수가 2배씩 증가합니다
몇일만에 창고의 치즈가 모두 없어지고, 이때까지의 쥐는 모두 몇 마리인지를 구하는 코드를 작성하세요
- 치즈 1Box : 1kg 
'''
cheeseBox = 10
cheeseGram = cheeseBox * 1000
mouse = 2      # 쥐 객체수
day = 0        # 날짜수

while cheeseGram > 0 :
    day += 1
    eat = mouse * 20  # 하루에 먹은 치즈양
    cheeseGram -= eat
    print("{:3}일 - 먹은 양 : {:8} , 남은 양 : {:8}".format(day, eat, cheeseGram))
    if day % 10 == 0 :
        mouse *= 2
        print("쥐 객체 증가 :", mouse)
print("총 {}일 - 객체 수 : {}".format(day, mouse))













