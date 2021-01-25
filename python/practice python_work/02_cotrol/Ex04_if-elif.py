
'''
if elif 문
- if 조건식_a :
    조건식_a 가 참이면 실행
  elif 조건식_b :
    조건식_a 거짓, 조건식_b가 참이면 실행


else :
    상위에 모든 조건식이 거짓이면 실행
    > 필요없으면 사용하지 않아도 됨

>여러개의 조건식 중에서 하나만을 실행하거나, 한개의 구간을 세분화 할 때 사용

'''
'''-----------------------------------------------------------------
value = 17
print("value : {}".format(value))
print()

print("- if 여러개 -")
if value > 0 :
    print("0 보다 큰수")
if value > 10:
    print("10 보다 큰수")
if value > 20:
    print("20 보다 큰수")
print()

print("- if elif -")
if value > 0 :
    print("0 보다 큰수")
elif value > 10 :
    print("10 보다 큰수")
elif value > 20 :
    print("20 보다 큰수")

-----------------------------------------------------------------'''


'''----------------------------------------

data = 5
print("data: ", data)
print()

if data >= 1 and data <= 10 :
    print("1~10")
if data >= 11 and data <= 20 :
    print("11~20")
if data >= 21 and data <= 30 :
    print("21~30")
print()


if data <= 10 :
    print("1~10")
elif data <= 20 :
    print("11~21")
elif data <= 30 :
    print("21~30")
------------------------------------'''


num = 15 # 잘못된 조건식
print("num : ", num)
print()

if num % 3 ==0 :
    print("3의 배수")
elif num % 5 == 0:
    print("5의 배수")
elif num % 3 == 0 and num % 5 == 0:
    print("3 and 5 의 배수")

print() 

num = 15
print("num : ", num)
print()


if num % 3 == 0 and num % 5 == 0:
    print("3 and 5 의 배수")
elif num % 3 ==0 :
    print("3의 배수")
elif num % 5 == 0:
    print("5의 배수")

print()


