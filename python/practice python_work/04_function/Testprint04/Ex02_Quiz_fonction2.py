'''
반지름 값을 넘겨 받아서 넓이를 구하는 함수를 구현
- 기본 반지름은 2 입니다.

'''
# def circle(radius = 2):
#     res = radius * radius * 3.14
#     print("반지름 {} 인 원의 넓이 : {}".format(radius, res))

# circle()
# circle(5)

'''
지수승 값을 계산하는 함수를 구현
- 기본값은 2 의 제곱
'''
# def powNums( a = 2, b = 2):
#     res = pow( a, b)
#     return res

# print(powNums(2, 3))


'''
데이터 평균을 구하는 함수를 구현
- 데이터의 수는 지정되어 있지 않음
'''
# def average(*nums):
#     print(nums)
#     plusNums = 0
#     count = 0
#     for i in nums:
#         plusNums += i 
#         count += 1
#     averageRes = plusNums / count
    
#     return averageRes

# print(average(1,3))


'''
급여를 계산하는 함수를 구현
- 기본 근무 일수 : 30일, 기본 시간당 급여 :8590원
- 기본 급여, 시간당 급여를 구할 수 있음

1. 기본급여   2. 시간당 급여
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
