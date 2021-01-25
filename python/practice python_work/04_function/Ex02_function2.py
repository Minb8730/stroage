'''
디폴트 매개변수
- 함수의 매개변수에 기본값을 지정해서 정의하는 함수를 말함.
- 호출부에서 넘어오는 인자값은 매개변수의 왼쪽에서부터 순서대로 넘겨받기 때문에
  디폴트 인자값의 지정은 오른쪽에서부터 해야 한다.
'''
# def hi(message = "hello"):
#     print(message)

# hi(17)
# hi()
# print()

# def calcSum(v1 =1, v2 =2):
#     res = v1 + v2
#     print("{} + {} = {}".format(v1, v2, res))

# calcSum()
# calcSum(11)
# calcSum(22, 33)


'''
keyword Arguments
- 함수 호출시에 매개변수를 지정해서 값을 넘겨주는 방식
- 호출부에서 넘어오는 인자값은 매개변수의 왼쪽에서부터 순서대로 전달
    그러나 keyword Argument를 사용하면 순서에 상관없이 매개변수를 지정해서 값을 전달 할 수 있음

'''
# def memberGrade(name = "none", grade = "일반"):
#     print("{} - {}".format(name, grade))

# memberGrade("추신수")
# memberGrade(grade = "vip", name = "손흥민") #순서는 상관없다.
# memberGrade(grade = "none")

'''
가변 인자
- 함수에서 몇개의 인자값을 받을지 정하지 못했을 때 사용
- 가변인수를 사용 할 때에는 '*' 을 붙여서 설정 # tuple로 처리됐음
'''

# def variFunc(*arg):
#     print(arg)
#     print("arg type :", type(arg))
#     print(arg[1])
#     arg = list(arg)

# variFunc(1, 2, 3)


'''
키워드 가변인자
- 가변인자처럼 사용하되 ' key : value ' 의 쌍으로 사용해야 함.
- 키워드 가변인자는 '**' 을 붙여서 설정
- 가변인수의 값은 내부적으로 dict로 처리됨
'''
def variDict(**arg):
    print(arg)
    print("arg type :", type(arg))
    for k, v in arg.items():
            print("key : {} - value : {}".format(k, v))


variDict(하나 = "1", 둘 ="2")