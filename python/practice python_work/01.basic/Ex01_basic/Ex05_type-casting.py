'''
자료형 (data type)
 - 데이터를 보관하고 있는 공간의 형식을 말한다.

type()
 - 변수에 저장되어 있는 데이터의 형태를 확인하는 함수

'''


'''
bool
- True(참), False(거짓)의 값을 가집니다.
'''
# ba = True
# print("ba :", ba)
# print("ba type :", type(ba))


'''
int(정수)
 - 양수, 음수의 숫자 값
'''
# ia = 10
# print("ia :", ia)
# print("ia type :", type(ia))

'''
float (실수)
- 소수점을 사용하는 숫자 값
'''
# fa = 1.2
# print("fa :", fa)
# print("fa type :", type(fa))

'''
str (문자열)
- 문자들의 집합
'''
# sa = "python"
# print("sa :", sa)
# print("sa type :", type(sa))


'''---------------------------------------------------------------------------------------------
자료형 변환
- 데이터의 자료형을 강제로 변환 할 수 있음.
    >변환 자료형(데이터)

'''

# print("- bool 변환 -")
# print(bool(1), bool(0), bool(-1)) # 1, -1 은 True 값, 0만 False 값을 가짐
# print(bool(1.2), bool(0.0), bool(-4.5))
# print(bool(' '), bool('a'), bool('')) #아무것도 없는 빈공백 3번째만 False 나머지는 True 값

# va = 10
# vb = bool(va)
# print("va : {}, vb : {}".format(va, vb))

# print(" - int 변환 -") #숫자로 이루어진 문자열만 int 타입으로 형변환이 가능
# print(int(True), int(False))
# print(int("123"), int("-7"), int("0"))
# print(int(12.34))

# print("- float 변환 -")
# print(float(True), float(False))
# print(float("1.2"), float("-3.4")) #소숫점까지 나타냄

print("- str 변환 -")
print(str(123))

data = 123
print(data + 100)
print("data type:", type(data))

data = str(data)
# print(data + 100) #data 를 문자 타입으로 변환했기 때문에 에러가 난다.
print("data type :", type(data))