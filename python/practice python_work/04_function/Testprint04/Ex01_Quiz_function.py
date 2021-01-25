'''
입력 허용 범위값(시작, 종료)을 넘겨받아서, 해당 범위안의 숫자를 입력받아서 반환하는 함수를 구현
'''
# def rangeA ( a, b):
#     print(range( a, b+1))


'''
1~10 사이의 랜덤값을 사용해서 변수 2개를 각각 초기화
두수를 넘겨받아서, 두수중 큰수를 찾아서 반환하는 함수를 구현
'''
# from random import*
# def randNum():
#     a = randint(1, 10)
#     b = randint(1, 10)
#     if a > b:
#         return a
#     elif a < b:
#         return b
#     else:
#         return print("a와 b의 값이 같습니다.")

# print(randNum())



'''
입력 받을 형태의 문자열 값을 넘겨받아서, 해당 문자열 타입의 값을 입력받아서 변환하는 함수를 구현
- 정수, 실수, 문자열
'''

# def typeFind():
#     text = input("입력할 문자 > ")
    
#     if type(text) == type(chr(text)):
        



'''
사칙연산( +, -, *, /) 기호와 숫자 2개를 넘겨받아서, 해당 연산 결과를 반환하는 함수를 구현
'''

def numsPlay():
    a = int(input("숫자 입력 > "))
    b = input("+, -, *, / 입력 > ")
    c = int(input("숫자 입력 > "))

    # if type(a) != type(chr(a)) and type(c) != type(chr(b)):
    #     print("숫자를 기입해 주세요.")
    if b == "+":
        plus = a + c 
        print("{} {} {} = {}".format(a, b, c, plus))
        return plus
    elif b == "-":
        minus = a - c 
        print("{} {} {} = {}".format(a, b, c, minus))
        return minus
    elif b == "*":
        multi = a * c 
        print("{} {} {} = {}".format(a, b, c, multi))
        return multi
    elif b == "/":
        devine = a / c 
        print("{} {} {} = {}".format(a, b, c, devine))
        return devine

numsPlay()

    # print("{} {} {} = {}".format(a, b, c))






