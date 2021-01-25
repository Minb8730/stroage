'''
가수이름 (key), 노래 제목(value) 를 입력받아서 저장하고, 출력하는 코드를 작성

'''
# singer = input("가수 이름 > ")
# song_name = input("노래 제목 > ")

# song = dict()

# song.setdefault(singer, song_name)

# print(song)




'''
음식 칼로리 파일의 내용을 사용해서 아래의 문제를 해결

1. 입력을 사용해서 데이터를 저장 할 수 있음
    >데이터 구성 : 음식명(key) : 칼로리(value)

2. 저장된 데이터를 출력하는 코드를 작성
3. 음식 이름을 사용해서 해당 음식의 칼로리를 확인하는 코드를 작성
4. 음식 이름을 사용해서 해당 음식을 삭제하는 코드를 작성
5. 음식 이름, 변경 칼로리를 사용해서 해당 음식의 칼로리를 수정하는 코드를 작성
'''



# # 1. 입력을 사용해서 데이터를 저장 할 수 있음
# #     >데이터 구성 : 음식명(key) : 칼로리(value)


# food = dict()
# food.update({"카페오레" : 57, "홍차" : 0, "우유" : 122, "요구르트" : 45, "콜라" : 97 })

# print("----- 음식 - 칼로리 ----")
# for item in food.items():
#     k,v = item
#     print("{} - {} kcal".format(k, v))

# print("---- 음식 추가 ----")
# food_name = input("음식 이름 > ")
# kcal = input("칼로리 > ")


# food.setdefault(food_name, kcal)

# # 2. 저장된 데이터를 출력하는 코드를 작성
# print(food)

# # 3. 음식 이름을 사용해서 해당 음식의 칼로리를 확인하는 코드를 작성

# check_food = input("확인 할 음식 이름 > ")
# if check_food in food:
#     for k,v in food.items():
#         if k == check_food:
#             print("{0} 의 칼로리는 {1}kcal 입니다".format(k, v))
# else:
#     print("목록에 없는 음식입니다.")



# # 4. 음식 이름을 사용해서 해당 음식을 삭제하는 코드를 작성

# remove_food = input("삭제 할 음식 이름 > ")
# if remove_food in food:
#     food.pop(remove_food)
#     print("{} 가 목록에서 삭제 되었습니다.".format(remove_food))
#     print(food)
# else:
#     print("이미 목록에 없는 음식입니다.")


# # 5. 음식 이름, 변경 칼로리를 사용해서 해당 음식의 칼로리를 수정하는 코드를 작성

# change_cal = input("칼로리 변경 할 음식 이름 > ")
# if change_cal in food:
#     p,k = change_cal
#     cal2 = str(input("변경 할 칼로리 > "))
#     food[change_cal] = cal2
#     print("{} 의 칼로리는 {}cal 입니다".format(p, cal2))
# else:
#     print("목록에 없는 음식입니다.")
# print(food)



food = dict()
food.update({"카페오레" : 57, "홍차" : 0, "우유" : 122, "요구르트" : 45, "콜라" : 97 })


foodRun = True
while foodRun:
    print("1.추가   2.삭제  3.kcal 수정    4.목록   0.종룍")
    select = int(input("선택 >> "))

    #추가
    if select == 1:
        print("---- 음식 추가 ----")
        food_name = input("음식 이름 > ")
        kcal = input("칼로리 > ")
        food.setdefault(food_name, kcal)
        print(food)

    #삭제
    elif select == 2:
        remove_food = input("삭제 할 음식 이름 > ")
        if remove_food in food:
            food.pop(remove_food)
            print("{} 가 목록에서 삭제 되었습니다.".format(remove_food))
            print(food)
        else:
            print("이미 목록에 없는 음식입니다.")

    #kcal 수정
    elif select == 3:
        change_cal = input("칼로리 변경 할 음식 이름 > ")
        if change_cal in food:
            p,k = change_cal
            cal2 = str(input("변경 할 칼로리 > "))
            food[change_cal] = cal2
            print("{} 의 칼로리는 {}cal 입니다".format(p, cal2))
        else:
            print("목록에 없는 음식입니다.")
        print(food)

    #음식 목록
    elif select == 4:
        print("----- 음식 - 칼로리 ----")
        for item in food.items():
            k,v = item
            print("{} - {} kcal".format(k, v))


    #종료
    elif select == 0:
        foodRun = False
    








