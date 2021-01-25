'''
1~ 30 사이의 3의 배수를 출력하는 코드를 작성
-단, 4의 배수도 되는 수는 출력되지 않음
'''

# for num in range(1, 31):
#     if num % 3 == 0:
#         if num % 4 == 0:
#             continue
#         print(num, end= " ")
    
'''
입력값이 홀수인지, 짝수인지 알려주는 코드를 작성
0이 입력되면 종료
'''

# while stop:
#     numA = int(input(">>"))
#     if numA == 0:
#         break
#     elif numA % 2 == 0:
#         print("{} : 짝수".format(numA))
#     else:
#         print("{} : 홀수".format(numA))
    
'''t
하나의 값으로 램프의 밝기를 변경하는 코드를 작성
Ex) t : 밝기 변경, e : 종료
    터치    : t
    lamp    : 약
    터치    : t
    lamp    : 강
    터치    : t
    lamp    : 꺼짐
    터치    : a
    터치    : t
    lamp    : 약
    터치    : e
   - power off 

'''


# bright = 0 # 0 : 꺼짐, 1 : 약, 2 : 강
# lampRun = True

# while lampRun:
#     touch = input("터치 >")
#     if touch == "0" or touch == "t":
#         if touch == 't':
#             if bright == 0:
#                 print("꺼짐")
#                 bright = 1
#             elif bright == 1:
#                 print("약")
#                 bright = 2
#             else :
#                 print("강")
#                 bright = 0
#         else:
#             lampRun = False

# else:
#     print(" - power off - ")






print("-------------------------------------------")
print("1.커피(300)  2.코코아(250")
print("-------------------------------------------")

price = 0
machine = True

coffee = "커피"
cocoa = "코코아"
money = int(input("금액을 투입하세요 >> "))
print(money)

while machine:
    print("1.커피(300)    2.코코아(250)     3.종료")
    choice = int(input())
    if choice == 1 :
        if money < 300 :
            print("잔액이 부족합니다.")
        else :
            print("{}가 나왔습니다.".format(coffee))
            money -= 300
    elif choice == 2 :
        if money < 250 :
            print("잔액이 부족합니다.")
        else :
            print("{}가 나왔습니다.".format(cocoa))
            money -= 250
    elif choice == 3 :
        break
    else :
        print("번호를 확인해 주세요.")
    print("거스름돈 : {} 원".format(money))
    print("1. 추가      2. 반환")
    choice = int(input())
    if choice == 1 :
        continue
    elif choice == 2 :
        print("거스름 돈 : {} 원".format(money))
        break






