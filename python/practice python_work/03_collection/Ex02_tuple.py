'''
collection
- 여러개의 데이터를 한곳에 모아 놓은 자료형을 말함.
- 순서형, 맵핑형, 집합형이 있음.
 
  > 순서형
    - 데이터에 index(번호) 를 붙여서 나열하는 데이터 구조
    - str(문자열), tuple(튜플), list(리스트)

  > 맵핑형
    - 데이터를 key를 사용해서 나열하는 구조
    - dict(사전)

  > 집합형
    - 단순하게 데이터를 한곳에 모아놓은 구조
    - set(집합)


        자료형      데이터수정      접근방식
문자열   str        가능           sequence
튜플     tuple      불가능         sequence 
리스트   list       가능           sequence
사전     dict       가능           mapping( kye - value )
집합     set        가능           set( 중복 x )

'''

'''
tuple
    - tuple 은 여러가지 데이터를 순서있게 저장하지만, 한번 설정한 값은 수정 할 수 없음
    - tuple 을 생성할 때에는 ()를 사용하고, ',' 를 사용해서 데이터를 나열
    - tuple 을 생성할 때 값이 하나이면 데이터 뒤에 ',' 를 사용해야 합니다.
    - tuple 생성시에는 () 를 사용하지 않아도 됩니다.

'''
# #중복된 값을 저장할 수 없음.

# #tuple
# tu1 = (1, 2, 3, 4, 5)
# print("tu1 :", tu1)

# tu2 = ('a', 'b', 'c', 'd', 'e')
# print("tu2 :", tu2)

# tu3 = ( 1, 'one', '하나', 1.0)
# print("tu3 :", tu3)

# tu4 = ("good") # 튜플이 아니다.
# print("tu4 :", tu4)
# print("tu4 type :", type(tu4))
# # 튜플로 사용하고 싶으면 ("good",) 쉼표를 추가해주어야 한다.

# tu5 = 1, 2, 3
# print("tu5 :", tu5)

'''
unpacking
    - tuple 의 요소들을 분리해서 각각의 변수에 넣어 줄 수 있음.
    이때 변수의 개수는 tuple의 요소의 수와 같아야 함.
'''

# fruits = "사과", "바나나", "망고"
# print("fruits :", fruits)

# apple, banana, mango = fruits
# print("apple :", apple)
# print("banana :", banana)
# print("mango :", mango)


'''
index
    - tuple 안의 하나의 요소에 접근 할 때 사용
    > tuple 명 [ index ]
    - index는 0 부터 시작
'''

# lower = 'a', 'b', 'c', 'd', 'e'
# print("lower :", lower)
# print("lower[2] :". lower[2])

'''
슬라이싱
    -tuple 안의 일정 부분의 요소를 선택 (자르기)
    -tuple[ 시작index : 종료index : step]
    > 실제 종료 index는 '종료index -1'
    step의 기본값은 1씩 증가

'''

# num = 1, 2, 3, 4, 5
# print("num :", num)
# print("num[1 : 3] :", num[1:3])
# print("num[2 : ]", num[2:])
# print("num[ ::2]",num[::2])

'''
tuple 연산
'''

# tu_n = 1, 2, 3
# tu_a = 'a', 'b'
# print("tu_n :", tu_n)
# print("tu_a :", tu_a)
# print()
# tu_all = tu_n + tu_a
# print("tu_all :", tu_all)
# print()

# print("3 in tu_all", 3 in tu_all)
# print("3 not in tu_all", 3 not in tu_all)


'''
for 문 적용
'''

# name_tu = "추신수", "유재석", "손흥민"
# print("name_tu :", name_tu)
# print()
# for el in name_tu:
#     print(el)
# print()

# nameCnt = len(name_tu)
# print("name_tu 요소의 수 :", nameCnt)
# print()

# for idx in range(len(name_tu)):
#     print(name_tu[idx])


'''
n차 tuple
'''

data = ((1, "하나"), (2, "둘"), (3, "셋"))
print("data :", data)
print()

print("data[0] :", data[0])
print("data[0][1] :", data[0][1])
print("data[2][0] :", data[2][0])


ra, rb, rc = data
print("ra :", ra)
print("rb :", rb)
print("rc :", rc)

e1, e2 = ra
print(e1, e2)

for r in data:
    print(r)

for r in data:
    for c in r:
        print(c, end = " ")
    print()

for el in data:
    e1, e2 = el
    print(e1, e2, sep = " - ")
print()