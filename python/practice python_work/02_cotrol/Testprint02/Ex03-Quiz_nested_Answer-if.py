

# Ex03-Quiz_nested-if.py

'''
태어난 년도를 사용해서 나이를 구하고, 나이를 사용해서 성인과 미성년자를 구분합니다
이때, 성인이면 청년층(20 ~ 39)과 중장년층(40 이상)으로 분류하고, 미성년자이면 청소년(14 ~19)과 어린이(0 ~ 13)로 분류하는 코드를 작성하세요
'''
# userYear = int(input("태어난 년도 입력 > "))
# userAge = 2020 - userYear + 1
# print("나이 : {} 세".format(userAge))
# print()

# if userAge > 19 :
#     print("성인 - ", end= "")
#     if userAge < 40 :
#         print("청년층")
#     else :
#         print("중장년층")
# else :
#     print("미성년자 - ", end="")
#     if userAge >= 14 :
#         print("청소년")
#     else :
#         print("어린이")


'''
보유한 금액에 따라서 구매 할 있는 아이템 목록을 보여주는 코드를 작성하세요
- 3000 미만
  > 쇠검 - 일반물약 - 쇠방패
  3000 이상
  > 광선검 - 에너지 드링크 - 방어막
- 3000 이상이면 전체 아이템 목록이 나와야 합니다
'''
# money = int(input("보유 금액 입력 > "))
# print("금액 : {} 원".format(money))
# print()

# print("--- 아이템 목록 ---")
# if money >= 0:
#     print("쇠검 - 일반물약 - 쇠방패")
#     if money >= 3000:
#         print("광선검 - 에너지 드링크 - 방어막")


'''
제품의 크기, 무게를 이용해서 사용한 가능한 cart 를 알려주는 코드를 작성하세요
- 크기         무게       cart
  small       50kg 미만  cart-A
  small       50kg 이상  cart-B
  large       50kg 미만  cart-C
  large       50kg 이상  cart-D
'''
cart =""
size = input("크기 입력 > ")

if size == 'small' or size == 'large':
    weight = float(input("무게 입력 > "))
    print()
    print("크기 : {} - 무게 : {}kg".format(size, weight))
    if size == "small":
        if weight < 50:
            cart = "cart-A"
        else:
            cart = "cart-B"
    else:
        if weight < 50:
            cart = "cart-C"
        else:
            cart = "cart-D"
    print("{}를 사용하세요..".format(cart))
else:
    print("크기 선택 오류~")

    






























