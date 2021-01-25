

# Ex01-Quiz_function.py

from random import randint

'''
입력 허용 범위값(시작, 종료)을 넘겨받아서, 해당 범위안의 숫자를 입력받아서 반환하는 함수를 구현하세요
'''
# def inputInteger(start, end):
#     while True:
#         value = input("{} ~ {} 사이의 수 입력 > ".format(start, end))
#         if value.isdecimal():
#             value = int(value)
#             if value >= start and value <= end:
#                 break
#     return value

# iv = inputInteger(1, 10)
# print("iv :", iv)


'''
1 ~ 10 사이의 랜덤값을 사용해서 변수 2개를 각각 초기화합니다
두수를 넘겨받아서, 두수중 큰수를 찾아서 반환하는 함수를 구현하세요
'''
# def findMax(a, b):
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     else:
#         return 0

# dataA = randint(1, 5)
# dataB = randint(1, 5)
# maxData = findMax(dataA, dataB)
# if maxData != 0:
#     print("{}, {} 중 큰수 : {}".format(dataA, dataB, maxData))
# else:
#     print("{}, {} 같은수".format(dataA, dataB))
# print()



'''
입력 받을 형태의 문자열 값을 넘겨받아서, 해당 문자열 타입의 값을 입력받아서 반환하는 함수르 구현하세요
- 정수, 실수, 문자열
'''
# def typeInput(type):
#     data = ""
#     if type == "정수":
#         data = int(input("숫자 입력 > "))
#     elif type == "실수":
#         data = float(input("실수 입력 > "))
#     elif type == "문자열":
#         data = input("단어 입력 > ")
#     return data
    
# type = input("입력 타입 > ")
# value = typeInput(type)
# print("입력 값 :", value)



'''
사칙연산( + , - , * , / ) 기호와 숫자 2개를 넘겨받아서, 해당 연산 결과를 반환하는 함수를 구현하세요
'''
def inputInteger(start, end):
    while True:
        value = input("{} ~ {} 사이의 수 입력 > ".format(start, end))
        if value.isdecimal():
            value = int(value)
            if value >= start and value <= end:
                break
    return value

def calcRun(opt, a, b):
    res = ""
    if opt == '+':
        res = a + b
    elif opt == '-':
        res = a - b
    elif opt == '*':
        res = a * b
    elif opt == '/':
        res = a / b
    else:
        print("연산자 선택 오류~")
    return res
    
opt = input("+ , - , * , /  선택 > ")
va = inputInteger(1, 10)
vb = inputInteger(1, 10)
res = calcRun(opt, va, vb)
print("결과 :", res)
\



























