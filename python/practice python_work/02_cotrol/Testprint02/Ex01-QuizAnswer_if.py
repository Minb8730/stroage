

# Ex01-Quiz_if.py

'''
Q-1 두수 중 큰수를 차는 코드를 작성하세요
    - 두수는 다른 수 입니다( if문으로 구현하세요 )
'''
# v1 = int(input("첫번째 숫자 입력 > "))
# v2 = int(input("두번째 숫자 입력 > "))
# print()

# max = 0
# if v1 > v2:
#     max = v1
# if v2 > v1:
#     max = v2
# print("{}, {} 큰수 : {}".format(v1, v2, max))


'''
Q-2 세개의 수 중에서 큰수를 찾는 코드를 작성하세요
    - 세개의 수는 모두 다른 수 입니다
'''
# v1 = int(input("첫번째 숫자 입력 > "))
# v2 = int(input("두번째 숫자 입력 > "))
# v3 = int(input("세번째 숫자 입력 > "))
# print()

# max = 0
# # if v1 > v2:
# #     max = v1
# # if v2 > v1:
# #     max = v2
# # if v3 > max:
# #     max = v3
# if v1 > v2 and v1 > v3:
#     max = v1
# if v2 > v1 and v2 > v3:
#     max = v2
# if v3 > v1 and v3 > v2:
#     max = v3
# print("{}, {}, {} 중 큰수 : {}".format(v1, v2, v3, max))


'''
Q-3 5의 배수인지를 확인하는 코드를 작성하세요
'''
# v3 = int(input("숫자 입력 > "))

# if v3 % 5 == 0 :
#     print("{} : 5의 배수".format(v3))
# if v3 % 5 != 0 :
#     print("{} : 5의 배수가 아니에요..".format(v3))


'''
Q-4 두수의 합이 2의 배수이면서 3의 배수도 되는지를 확인하는 코드를 작성하세요
'''
# v1 = int(input("첫번째 숫자 입력 > "))
# v2 = int(input("두번째 숫자 입력 > "))
# print()

# sum = v1 + v2
# print("합 :", sum)
# if sum % 2 == 0 and sum % 3 == 0:
#     print("2 and 3의 배수")
# if sum % 2 != 0 or sum % 3 != 0:
#     print("2 or 3의 배수가 아니에요..")


'''
Q-5 두 위치 사이의 거리를 구하는 코드를 작성하세요
    - 거리의 결과는 + 값으로 나와야 합니다
'''
p1 = int(input("첫번째 위치 입력 > "))
p2 = int(input("두번째 위치 입력 > "))

distance = p1 - p2
if p2 > p1:
    distance = p2 - p1
print("거리 : {}".format(distance))




































