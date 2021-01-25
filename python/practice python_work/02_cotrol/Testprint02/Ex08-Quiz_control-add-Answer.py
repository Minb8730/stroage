

'''
1 ~ 30 사이의 3의 배수를 출력하는 코드를 작성하세요
- 단, 4의 배수도 되는 수는 출력되지 않습니다
'''
# for v in range(1, 31):
#     if v % 3 == 0:
#         if v % 4 == 0:
#             continue
#         print(v, end=" ")

# print()


'''
입력값이 홀수인지, 짝수인지를 알려주는 코드를 작성하세요
0이 입력되면 종료됩니다
'''
# while True:
#     data = int(input("숫자 입력 > "))
#     if data == 0:
#         break
#     elif data % 2 == 1:
#         print("{} : 홀수".format(data))
#     elif data % 2 == 0:
#         print("{} : 짝수".format(data))

# print()



'''
하나의 값으로 램프의 밝기를 변경하는 코드를 작성하세요
Ex) t : 밝기 변경, e : 종료
    터치  : t
    lamp : 약
    터치  : t
    lamp : 강
    터치  : t
    lamp : 꺼짐
    터치  : a
    터치  : t
    lamp : 약
    터치  : e
    - Power off -
'''
# bright = 0  # 0 : 꺼짐, 1 : 약, 2 : 강
# lampRun = True

# while lampRun:
#     touch = input("터치 > ")
#     if touch == 'e' or touch == 't':
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
#     print("- Power off -")



'''
자판기.png 파일의 내용을 구현하세요
'''
coffee = 300
cocoa = 250

print("1.커피({})  2.코코아({})".format(coffee, cocoa))
money = int(input("금액을 투입하세요 > "))
print()

while money >= cocoa:
    print("1.커피({})  2.코코아({})  3.종료".format(coffee, cocoa))
    select = int(input("선택 >> ")) 

    if select == 1:
        if money >= coffee:
            money -= coffee
            print("커피카 나옵니다~")
        else:
            print("금액이 부족합니다~")
    elif select == 2:
        if money >= cocoa:
            money -= cocoa
            print("코코아가 나옵니다~")
        else:
            print("금액이 부족합니다~")
    elif select == 3:
        break

    # 추가 구매
    if money >= cocoa:
        print("남은 금액 : {} 원".format(money))
        purchase = True
        while purchase:
            buy = int(input("1.추가구매  2.반환 > "))
            if buy == 1:
                break
            elif buy == 2:
                purchase = False
        else:
            break
    print()


print("거스름 돈 : {} 원".format(money))

























