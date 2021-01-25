

# Ex03-Quiz_list.py

from random import randint

'''
반복문을 사용해서 list의 값을 출력하는 코드를 작성하세요
ex_ls = [ 'a', 'b', 'c', 'd', 'e' ]
'''
# ex_ls = [ 'a', 'b', 'c', 'd', 'e' ]
# for v in ex_ls:
#     print(v, end= " ")
# print()


'''
1 ~ 10까지의 숫자가 저장된 리스트를 생성하는 코드를 작성하세요
'''
# n_ls = list(range(1, 11))
# print("n_ls :", n_ls)
# print()

# n_ls.clear()

# for v in range(10):
#     n_ls.append(v + 1)
# print("n_ls :", n_ls)
# print()


'''
리스트에 5개의 숫자를 입력(랜덤값 사용가능)받아서 저장하고, 저장된 데이터의 합을 구하는 코드를 작성하세요
'''
# data = list(range(5))
# sum = 0
# for idx in range(len(data)):
#     data[idx] = randint(1, 10)
#     print(data[idx], end=' ')
#     sum += data[idx]
# print()
# print("합 :", sum)


'''
대문자 A ~ Z가 저장된 list를 생성하는 코드를 작성하세요
'''
# text = list()
# for v in range(ord('A'), ord('Z')+1):
#     text.append(chr(v))
# print()
# print("text :", text)
# print()



'''
1 ~ 100 사이의 랜덤값 10개가 저장된 list를 작성하세요
'''
size = 10
value = list(range(size))

for idx in range(size):
    value[idx] = randint(1, 101)
print(value)


































