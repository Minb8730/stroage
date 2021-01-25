'''

태어난 년도를 사용해서 나이를 구하고, 나이를 사용해서 성인과 미성년자를 구분합니다.
이때, 성인이면 청년층(20~39)과 중장년층(40 이상)으로 분류하고, 미성년자이면 청소년(14~19)과 어린이(0~13)로 분류하는 코드를 작성
'''

'''
year = int(input("태어난 년도를 입력하세요. "))
age = 2021 - year
print("{}세".format(age))

if age > 19 :
    print("성인입니다.", end =" ")
    if age < 40 :
        print("본인은 청년층입니다.")    
    else :
        print("본인은 장년층입니다.")

else :
    if age>=14:
        print("본인은 청소년입니다.")
    else :
        print("본인은 청년층입니다.")

print()

'''
'''
보유한 금액에 따라서 구매 할 수 있는 아이템 목록을 보여주는 코드를 작성하세요
~3000 미만
> 쇠검 - 일반물약 - 쇠방패
3000 이상
> 광선검 - 에너지 드링크 - 방어막
-3000 이상이면 전체 아이템 목록이 나와야 합니다.
'''

money = int(input("현재 보유한 본을 입력하세요. "))
print("현재 보유한 돈은 {} 원입니다.".format(money))
print()

print("- 구매 할 수 있는 아이템 목록 -")
if  money < 3000 :
    print("쇠검 - 일반물약 - 쇠방패")

else :
    print("쇠검 - 일반물약 - 쇠방패")
    print("광선검 - 에너지 드링크 - 방어막")

print()


'''
제품의 크기, 무게를 이용해서 사용 가능한 cart 를 알려주는 코드를 작성
-크기       무게        cart
small       50kg 미만   cart-A
small       50kg 이상   cart-B
large       50kg 미만   cart-C
large       50kg 이상   cart-D
'''

size = str(input("사이즈를 입력하세요."))

weight = float(input("무게를 입력하세요. "))


 
if size == "small" :
    if weight < 50 :
        print("cart-A를 사용해주세요.")
    else :
        print("cart-B를 사용해주세요.")

if size == "large" :
    if weight < 50 :
        print("cart-C를 사용해주세요.")
    else :
        print("cart-D를 사용해주세요.")




