from random import randint, randrange

'''
입력받은 숫자 크기의 리스트를 생성하고, 생성된 리스트에 값을 입/출력하는 코드를 작성
'''
# size = int(input("리스트의 크기 :"))
# lstA = list(range(size))

# for i in range(size):
#     lstA[i] = randint(1, 50)

# print(lstA)


'''
아래의 tuple 에서 길이가 5인 요소만 list 에 저장하는 코드를 작성
'''

# data_tu = 'alpha', 'bravo', 'chalie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel'
# lstB = list(data_tu)
# for i2 in lstB:
#     if len(i2) == 5:
#         print(i2, end =" ") 


'''
list 에서 점수가 60점 미만인 학생들을 따로 모은 list를 만드는 코드를 작성
'''

stu = [ ('박보검', 87), ('박신혜', 65), ('송중기', 53),
        ('이민정', 45), ('이병헌', 89), ('소지섭', 57) ]

# for v1 in stu:
#     student, score = v1
#     if score < 60:
#         print(student, score, end = " ")



'''
1 ~ 10 사이의 랜덤값 10개를 list에 저장합니다
중복된 값은 들어갈 수 없으며, 숫자 7이 있는 곳의 위치를 찾는 코드를 작성하세요
'''
# size = 10
# lstD = list()


# for i in range(size):
#     q = randint(1, 10)
#     while lstD.count(q) >= 1:
#         q = randint(1, 10)
#     lstD.append(q)
# print(lstD)
# sevenidx = lstD.index(7)
# print(sevenidx+1)


# data = list(range(1, size +1))
# myList = list()

# for cnt in range(size):
#     idx = randrange(len(data))
#     select = data.pop(idx)
#     myList.append(select)
# #print(myList)




'''
로또 번호를 생성하는 코드를 작성
- 1~45 사이의 랜덤값 6개 (중복 X)
- 결과는 오름차순 정렬해서 출력
'''
size = 6
lstL =list(range(size)) 
lstM = list()
for i in range(size):
    lstL[i] = randint(1, 45)
    nums = lstL

lstM.append(nums)

lstM.sort()
print(lstM)

'''
사칙연산 3문제를 자동으로 출제하는 코드를 작성하세요
- 문제에 사용되는 숫자는 1 ~ 9까지 입니다
- 정답을 맞추면 결과 list에 0을 저장하고, 틀리면 X를 저장합니다
'''
# for i in range(3):
#     # 랜덤 숫자 2개
#     numA = randint(1, 9)
#     numB = randint(1, 9)
#     res = 0
#     #부호 정하기
#     signal = randint(1, 4)
#     if signal == 1:
#         res = numA + numB
#         signal = "+"
#     elif signal == 2:
#         res = numA - numB
#         signal = "-"
#     if signal == 3:
#         res = numA * numB
#         signal = "*"
#     if signal == 4:
#         res = numA / numB
#         signal = "/"

# #계산 식

#     print("{}번 문제 : {} {} {} = ".format(i, numA, signal, numB))
#     user = int(input())
#     if user == res:
#         print("정답")
#     else:
#         print("틀렸습니다.")