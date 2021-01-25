

# Ex04-Quiz_list.py

from random import randint, randrange
import timeit

'''
입력받은 숫자 크기의 리스트를 생성하고, 생성된 리스트에 값을 입/출력하는 코드를 작성하세요
'''
# size = int(input("list 크기 입력 > "))
# q1_ls = list(range(size))

# for idx in range(size):
#     q1_ls[idx] = randint(1, 50)

# for v in q1_ls:
#     print(v, end=" ")
# print()


'''
아래의 tuple에서 길이가 5인 요소만 list 에 저장하는 코드를 작성하세요
'''
# data_tu = 'alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel'

# fList = list()
# for v in data_tu:
#     if len(v) == 5:
#         fList.append(v)
# print()
# print(fList)


'''
list 에서 점수가 60점 미만인 학생들을 따로 모은 list를 만드는 코드를 작성하세요
'''
# stu = [ ('박보검', 87), ('박신혜', 65), ('송중기', 53),
#         ('이민정', 45), ('이병헌', 89), ('소지섭', 57) ]
# dList = list()

# for v in stu:
#     if v[1] < 60:
#         dList.append(v)
# print("- 60점 미만 -")
# print(dList)



'''
1 ~ 10 사이의 랜덤값 10개를 list에 저장합니다
중복된 값은 들어갈 수 없으며, 숫자 7이 있는 곳의 위치를 찾는 코드를 작성하세요
'''

# size = 10

# t_start = timeit.default_timer()
# value_ls = list()
# for cnt in range(size):
#     rd = randint(1, size)
#     while value_ls.count(rd) >= 1: # 현재 생성된 값이 list에 있는지 확인
#         rd = randint(1, size)
#     value_ls.append(rd)
# #print(value_ls)
# t_end = timeit.default_timer()
# print("시간 :", t_end - t_start )

# sevenIdx = value_ls.index(7)
# print("7 위치 :",sevenIdx + 1)


# print()


# t_start = timeit.default_timer()
# data = list(range(1, size +1))
# myList = list()

# for cnt in range(size):
#     idx = randrange(len(data))
#     select = data.pop(idx)
#     myList.append(select)
# #print(myList)
# t_end = timeit.default_timer()
# print("시간 :", t_end - t_start )



'''
로또 번호를 생성하는 코드를 작성하세요
- 1 ~ 45 사이의 랜덤값 6개 ( 중복 X )
- 결과는 오름차순 정렬해서 출력하세요
'''
# no = 45
# no_ls = list(range(1, no+1))
# lotto_ls = list()

# for cnt in range(6):
#     idx = randrange(len(no_ls))
#     select = no_ls.pop(idx)
#     lotto_ls.append(select)
# lotto_ls.sort()
# print(lotto_ls)



'''
사칙연산 3문제를 자동으로 출제하는 코드를 작성하세요
- 문제에 사용되는 숫자는 1 ~ 9까지 입니다
- 정답을 맞추면 결과 list에 0을 저장하고, 틀리면 X를 저장합니다
'''
ox_ls = list()
for cnt in range(3):
    # 데이터 생성
    dataA = randint(1, 9)
    dataB = randint(1, 9)
    res = 0
    # 연산자 선택
    opt = randint(1, 4)
    if opt == 1:
        res = dataA + dataB
        opt = '+'
    elif opt == 2:
        res = dataA - dataB
        opt = '-'
    elif opt == 3:
        res = dataA * dataB
        opt = '*'
    else:
        res = dataA / dataB
        opt = '/'

    # 문제
    print("{} {} {} = ?".format(dataA, opt, dataB))
    user = int(input("입력 >> "))
    if user == res:
        print("정답 ^^")
        ox_ls.append("O")
    else:
        print("틀렸어요 ㅠㅠ")
        ox_ls.append("X")
    print()

else:
    print(ox_ls)
    


















