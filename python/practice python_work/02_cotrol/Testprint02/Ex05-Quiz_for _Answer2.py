

# Ex05-Quiz_for.py

'''
지정한 숫자 만큼의 '*'을 출력하는 코드를 작성하세요
- for 문이 한번 실행 할 때마다 별 하나씩 출력됩니다
'''
# star = 7
# for v in range( star ):
#     print('*', end="")
# print()


'''
1 ~ 30 까지의 수를 1씩 증가시키면서 한줄에 10개씩 출력하는 코드를 작성하세요
'''
# for v in range(1, 31):
#     print("{:3}".format(v), end=" ")
#     if v % 10 == 0:
#         print()
# print()


'''
지정한 구구단 값을 모두 출력하는 코드를 작성하세요
'''
# dan = int(input("구구단 입력 > "))
# print()

# for v in range(1, 10):
#     print("{} x {} = {}".format(dan, v, dan*v))
# print()



'''
두수의 범위안의 숫자의 합을 구하는 코드를 작성하세요
'''
# dataA = int(input("첫번째 숫자 입력 > "))
# dataB = int(input("두번째 숫자 입력 > "))
# print()

# tot = 0
# first = dataA
# last = dataB
# if dataA > dataB :
#     first = dataB
#     last = dataA
# for v in range(first , last + 1):
#     tot += v
# print("{} ~ {} 까지의 합 : {}".format(first, last, tot))


'''
알파벳 a ~ z 까지를 출력하는 코드를 작성하세요
for문이 한번 실행 될 때마다 알파벳 하나씩 출력됩니다
'''
# for v in range(ord('a'), ord('z') + 1):
#     print(chr(v), end="")
#     if chr(v) != 'z':
#         print(", ", end="")
# print()



'''
문자열 하나를 입력받고, 문자열에서 검색 할 문자를 입력 받습니다
문자열안에 검색문자가 몇개 있는지를 구하는 코드를 작성하세요
'''
# text = input("문장 입력 > ")
# search = input("검색 문자 입력 > ")
# print()

# count = 0
# for v in text:
#     if v == search :
#         count += 1
# print("{} 문자수 : {}".format(search, count))


'''
첫날에는 1원을 입금하고, 둘째날 부터는 전날의 2배씩 입금합니다
위와 같은 방식으로 30일동안 입금한 총 금액을 구하는 코드를 작성하세요
'''
# money = 0  # 입금액
# balance = 0 # 잔액
# for day in range(1, 31): 
#     if day == 1:
#         money = 1
#     else:
#         money *= 2
#     balance += money
#     print("{:3}일 - 입금 : {:10}원 , 잔액 : {:10}원".format(day, money, balance))
# print("총 입금액 : {} 원".format(balance))


"""-------------------------------------------------------"""


'''
*****
*****
*****
*****
*****
'''
# for s in range(1, 6):
#     print('*' * 5)
# print()


'''
*
**
***
****
*****
'''
# for s in range(1, 6):
#     print('*' * s)
# print()


'''
*****
****
***
**
*
'''
# for s in range(5, 0, -1):
#     print('*' * s)
# print()



'''
    *
   **
  ***
 ****
*****    
'''
for s in range(1, 6):
    print(' '*(5-s), end='')
    print('*' * s)
print()






















