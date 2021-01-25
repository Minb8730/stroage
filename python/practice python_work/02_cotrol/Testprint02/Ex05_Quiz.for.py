'''

지정한 숫자 만큼의 '*' 을 출력하는 코드를 작성
-for 문이 한번 실행 할 때만다 별 하나씩 출력
'''

# star = 7

# for v in range(star):
#     print('*', end = "")
# print()


'''

1~30 까지의 수를 1씩 증가시키면서 한줄에 10개씩 출력하는 코드를 작성

'''

# for i in range(1, 31):
#     print("{:3}".format(i), end = " ")
#     if i % 10 == 0:
#         print()
    

'''
지정한 구구단 값을 모두 출력하는 코드를 작성
'''
# dan = int(input())
# print("{} 단".format(dan))

# for i in range(1, 10):
#     print("{} x {} = {}".format( dan ,i, dan*i ))



'''
두수의 범위안의 숫자의 합을 구하는 코드를 작성
'''

# start = int(input("첫번째 숫자 입력 : "))
# end = int(input("두번째 숫자 입력 : "))
# sum = 0

# first = start
# second = end

# if end < start :
#     first = end

# for q in range(start, end+1):
#     sum += q     

# print("{} 와 {} 범위 안의 숫자의 합은 {} 입니다.".format(start, end, sum))






'''
알파벳 a~z 까지를 출력하는 코드를 작성
for문이 한번 실행 될 때마다 알파벳 하나씩 출력
'''

# for a in range(97, 123) :
#     trans = chr(a)
#     print(trans)


'''

문자열 하나를 입력받고, 문자열에서 검색 할 문자를 입력 받습니다.
문자열안에 검색문자가 몇개 있는지를 구하는 코드를 작성
'''

# sentence = input("문자 입력 :")
# search = input("검색 문자 입력 :")
# print()

# count = 0
# for k in sentence :
#     if k == search :
#         count += 1
# print("{} 문자수 : {}".format(search, count))





'''
첫날에는 1원을 입금하고, 둘째날 부터는 전날의 2배씩 입금합니다.
위와 같은 ㅂ아식으로 30일 동안 입금한 총 금액을 구하는 코드를 작성
'''
# money = 0  #입금
# balance = 0
# for day in range(1, 31):
#     if day == 1:
#         money = 1
#     else :
#         money *= 2
#     balance += money




'''
*****
*****
*****
*****
*****
'''
for a in range(1,6):
    print("*"*5)

'''
*
**
***
****
*****
'''

for a in range(1,6):
    print("*"*a)

'''
*****
****
***
**
*
'''


for a in range(1,6):
    print("*"*(6-a))

#또는

for a in range(5, 0, -1):
    print("*"*a)

'''
    *
   **
  ***
 ****
*****
'''
for a in range(1,6):
    a = "*"*a
    print("{:>5}".format(a))




# word = "abc"
# print("{}".format(word))
# print("{:5}".format(word))
# print("{:<5}#".format(word))
# print("{:^5}#".format(word))







