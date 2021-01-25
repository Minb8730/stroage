

# Ex02-Quiz_function2.py

'''
반지름 값을 넘겨 받아서 원의 넓이를 구하는 함수를 구현하세요
- 기본 반지름은 2 입니다
'''
# def circleArea( radius = 2 ):
#     res = radius * radius * 3.141592
#     print("반지름 {}인 원의 넓이 : {}".format(radius, res))
#     return res

# circleArea()
# circleArea(5)


'''
지수승 값을 계산하는 함수를 구현하세요
- 기본값은 2의 제곱입니다
'''
# def squareData(num=2, e=2):
#     res = num**e
#     print("{} 의 {}승 : {}".format(num, e, res))
#     return res

# squareData()
# squareData(3)
# squareData(2, 4)


'''
데이터 평균을 구하는 함수를 구현하세요
- 데이터의 수는 지정되어 있지 않습니다
'''
# def avgCalc(*data):
#     sum = 0
#     for v in data:
#         sum += v
#     avg = sum / len(data)
#     print(data)
#     print("평균 : {:.1f}".format(avg))
#     return avg

# avgCalc(2, 4, 4)
# print()


'''
급여를 계산하는 함수를 구현하세요
- 기본 근무 일수 : 30일, 기본 시간당 급여 : 8590원
- 기본 급여, 시간당 급여를 구할 수 있습니다

1.기본급여  2.시간당 급여
'''

def wageCalc(day=30, time=8, money=8590):
    salary = day * time * money
    return salary


def wage():
    salary = 0   # 급여
    select = int(input("1.기본 급여  2.시간당 급여 > "))

    if select == 1:
        salary = wageCalc()
    elif select == 2:
        time = int(input("일한 시간 입력 > "))
        salary = wageCalc(1, time)

    if select == 1 or select == 2:
        print("급여 : {} 원".format(salary))
    return salary

wage()
































