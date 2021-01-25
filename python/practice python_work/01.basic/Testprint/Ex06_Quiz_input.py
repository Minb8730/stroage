'''
ID 를 입력하고, 입력받은 ID를 사용해서 E-mail 주소를 생성
 -Ex) id 입력 > test
      E-mail : test@abc.com

이름, 나이, 전화번호를 입력받아서 출력

숫자 2개를 입력받아서 사칙연산( +, -, *, /) 결과를 출력하는 코드 작성

태어난 년도를 입력받아서 나이를 계산하는 코드 작성

키를 입력 받아서 표준체중을 구하는 코드 작성
 -표준 체중 = (키 - 100) * 0.9
'''

Id = input()
print("E-mail : {}@naver.com".format(Id))



name = input()
age = input()
call = input()
print("이름 : {}, 나이 : {}, 전화번호 : {}".format(name, age, call))


ia = int(input("첫번째 숫자 입력 >"))
ib = int(input("두번째 숫자 입력 >"))

print("{} + {} = {}".format(ia, ib, ia+ib))
print("{} - {} = {}".format(ia, ib, ia-ib))
print("{} * {} = {}".format(ia, ib, ia*ib))
print("{} / {} = {}".format(ia, ib, ia/ib))




year = int(input())
now_age = 2020
now_age-=year
print("{}살".format(now_age))


height = int(input())
ctweight = (height - 100) *0.9
print("표준 체중 : {:.1f}kg".format(ctweight))

