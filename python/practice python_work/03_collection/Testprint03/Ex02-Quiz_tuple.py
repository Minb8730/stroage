

# Ex02-Quiz_tuple.py

menu = (("라면", 3000), ("김밥", 3000), ("라볶이", 5000),
        ("오므라이스", 6000), ("돈까스", 6000), ("떡볶이", 4000))

print("-----  메   뉴  -----")
for name, price in menu:
    print("{} - {}".format(name, price))
print()

# '''
# 라면, 떡볶이의 가격을 출력하는 코드를 작성하세요
# '''

# print(menu[0][1], menu[5][1])

# '''
# 가격이 6000원인 음식을 모두 찾아서 출력하는 코드를 작성하세요
# '''
# for menuA, price in menu:
#     if price == 6000:
#         print(menuA)


# '''
# 가격이 4000원 이하인 음식을 모두 찾아서 출력하는 코드를 작성하세요
# '''
# for menuA, price in menu:
#     if price <= 4000:
#         print(menuA)



'''
음식 이름을 입력받아서 해당 음식의 가격을 출력하는 코드를 작성하세요
'''
# order = input("음식 입력 > ")

# for menuA, price in menu:
#     if menuA == order:
#         print(price)
    

'''
음식 이름을 입력받아서, 입력 받은 음식의 총 금액을 구하는 코드를 작성
- '종료' 를 입력하면 더 이상의 입력을 받지 않음
'''

WholePrise =0
select = True
while select:
    order = input("음식 입력 > ")
    for menuA, price in menu:
        if menuA == order:
            WholePrise += price
        elif order == "종료":
            select = False

print("음식의 총 금액은 {}원 입니다.".format(WholePrise))



























