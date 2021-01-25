text = "Test python"
print("text :", text)
print()

'''
문자열 슬라이싱
- 문자열[ begin : end : step]
'''
# print("text[0 : 3] :", text[0 : 3])
# print("text[5 : ] :", text[5 : ])
# print("text[:: 2] :", text[:: 2])

'''
변수명.upper()
- 소문자를 대문자로 변환합니다.
'''

# print("text.upper() :", text.upper())

'''
변수명.lower()
- 대문자를 소문자로 변환합니다.
'''
print("text.lower() :", text.lower())
print()

'''
변수명.title()
- 단어의 첫글자만 대문자로 변환합니다.
'''
print("text.title() :", text.title())
print()

'''
변수명.split( separator)
- 구분자를 기준으로 문자열을 분할해서 리스트에 저장한 뒤에 반환합니다.
    > 구분자는 문자열로 지정합니다. - 기본값 : 공백
'''

# food =  "떡볶이 순대 튀김 오뎅"
# print("food :", food)
# print("food.split()", food.split())
# print()

# course = "서울-대전-대구-부산"
# print("course :", course)
# print("course.split() :", course.split("-"))


'''
변수명.count(문자)
- 문자열에서 특정 문자의 문자수를 계산합니다.
'''
text = "aa bbb ccc"
# print("text :", text)
# print("text.count(\"b\") :", text.count("b"))

'''
변수명.find( 검색문자, 시작 index)
- 문자열에서 특정 문자를 찾아서 해당 문자의 index를 반환합니다.
    >찾는 문자가 없으면 -1을 반환
'''
print("c 위치 :", text.find("c"))
print()

'''
변수명.startwith()
- 문자열이 특정 단어로 시작하는지 확인해서, True or False 값으로 반환합니다.
'''
if text.startswith("a"):
    print("맞아요")
else:
    print("틀려요")

'''
데이터 확인
'''

data = "test"
print("data :", data)
print("data.isalpha() :", data.isalpha())       #모든 문자가 알파벳인지 확인
print("data.islower :", data.islower())         #모든 문자가 소문자인지 확인
print("data.isupper :", data.isupper())         #모든 문자가 대문자인지 확인
print("data.isdecimal :", data.isdecimal())     #모든 문자가 숫자형태인지 확인
print()

age = input("나이 입력 > ")
if age.isdecimal():
    age = int(age)
else:
    print("숫자만 사용")













