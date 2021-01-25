'''
입력 값을 list 추가
'''
# e1 = list()
# for v in range(3):
#     value = input("{}번째 입력 > ".format(v+1))
#     e1.append(value)
# print()
# print("e1 :", e1)
''' --------------------------------------------------------------------------------'''
# size = 2
# ex1 = list(range(size))

# for idx in range(size):
#     ex1[idx] = input("[{}] 입력 > ".format(idx))

# print('ex1 :', ex1)
''' --------------------------------------------------------------------------------'''

# test_tu = 1, 2, 3
# print("test_tu : ", test_tu)
# print()

# test_ls = list(test_tu)
# print("test_ls : ", test_ls)
# print()

# test_ls[1] = 10
# test_tu = tuple(test_ls)
# print("test_tu : ", test_tu)

''' --------------------------------------------------------------------------------'''

# ls2 = [[1, "하나"], [2, "둘"]]
# print("ls2 : ", ls2)
# print()

# print("ls2[0] : ", ls2[0])
# print("ls2[0][1] : ", ls2[0][1])
# print("ls2[1][0] : ", ls2[1][0])
''' --------------------------------------------------------------------------------'''

t1 =[("A", 'a'), ("B", 'b'), ("C", 'c')]
print("t1 : ", t1)
print("t1 데이터 수 : ", len(t1))

for e1 in t1:
    t1, t2 = e1
    print(t1, t2)
print()

