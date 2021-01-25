

# Ex06-Quiz_dict.py

'''
가수이름(key), 노래 제목(value)를 입려받아서 저장하고, 출력하는 코드를 작성하세요
'''
# sing = dict()
# name = input("가수 이름 입력 > ")
# title = input("노래 제목 입력 > ")
# sing.setdefault(name, title)
# print(sing)


'''
음식 칼로리 파일의 내용을 사용해서 아래의 문제를 해결하세요

1.입력을 사용해서 데이터를 저장 할 수 있습니다
  > 데이터 구성 : 음식명(key) : 칼로리(value)
2.저장된 데이터를 출력하는 코드를 작성하세요
3.음식 이름을 사용해서 해당 음식의 칼로리를 확인하는 코드를 작성하세요
4.음식 이름을 사용해서 해당 음식을 삭제하는 코드를 작성하세요
5.음식 이름, 변경 칼로리를 사용해서 해당 음식의 칼로리를 수정하는 코드를 작성하세요
'''
food = dict()
food.update({"카페오레":57, "홍차":0, "우유":122, "요구르트":45, "콜라":97})
print(food)
print()

print("---  음식  리스트  ---")
for item in food.items():
    k, v = item
    print("{} - {} kcal". format(k, v))
print()

"""-----------------------------------------------------------------"""

# print("---  음식  추가  ---")
# fname = input("음식 이름 입력 > ")
# fkcal = input("칼로리 입력 > ")
# food.setdefault(fname, fkcal)
# print()

# print("---  음식  리스트  ---")
# for item in food.items():
#     k, v = item
#     print("{} - {} kcal". format(k, v))
# print()

"""-----------------------------------------------------------------"""

# print("---  칼로리  확인  ---")
# search = input("음식 이름 입력 > ")
# if search in food:
#     for k, v in food.items():
#         if k == search:
#             print("{} - {} kcal".format(k, v))
# else:
#     print("없는 음식입니다~")
# print()

"""-----------------------------------------------------------------"""

# print("---  음식  삭제  ---")
# fdel = input("음식 이름 입력 > ")
# if fdel in food:
#     food.pop(fdel)
#     print("{} 삭제".format(fdel))
# else:
#     print("없는 음식입니다~")
# print()

# print("---  음식  리스트  ---")
# for item in food.items():
#     k, v = item
#     print("{} - {} kcal". format(k, v))
# print()

"""-----------------------------------------------------------------"""

print("---  음식 칼로리 수정  ---")
falter = input("음식 이름 입력 > ")
if falter in food:
    kalter = int(input("변경 kcal 입력 > "))
    food[falter] = kalter
else:
    print("없는 음식입니다~")
print()

print("---  음식  리스트  ---")
for item in food.items():
    k, v = item
    print("{} - {} kcal". format(k, v))
print()























