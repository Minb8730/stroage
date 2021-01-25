'''
이름, 나이, 키를 변수에 저장해서 출력하는 코드를 작성
키는 소수점 첫째자리까지만 출력
'''

name = "민성기"
age = "27"
height = 181.745

print("이름 :", name)
print("나이 : {}세".format(age))
print("키 : {:.1f}".format(height))


'''
오늘 날짜의 년월일만 변수에 저장해서 출력
'''

year = 2020
month = 12
day = 16

print("{}년 {}월 {}일".format(year, month, day))

'''
아래의 제품이름과 가격을 각각 변수에 저장해서 출력하는 코드를 작성
--- 제품목록 ---
bluetooth 5.8   8000
ssd 512 G       120000
'''


Product1 = "bluetooth 5.8"
Product2 = "ssd 512 G"
Cost1 = 8000
Cost2 = 120000

# print("--- 제품목록 ---")
# print(Product1, end = "   ")
# print(Cost1)
# print(Product2, end = "   ")
# print(Cost2)

print("{:20}    {:10}".format(Product1, Cost1))