from random import*

'''
반복문을 사용해서 list 의 값을 출력하는 코드를 작성
ex_ls = ['a', 'b', 'c', 'd', 'e']
'''

# ls1 = ['a', 'b', 'c', 'd', 'e']
# lst2 =[]
# for i in ls1:
#    lst2.append(i)
# print(lst2)


'''
1 ~ 10 까지의 숫자가 저장된 리스트를 생성하는 코드를 작성
'''
# lstA = list(range(1, 11))
# print(lstA)



'''
리스트에 5개의 숫자를 입력(랜덤값 사용가능) 받아서 저장하고, 저장된 데이터의 합을 구하는 코드를 작성
'''
# al = 0
# size = list(range(5))
# for i in range(len(size)):
#     size[i] = randint(1, 10)
#     print(size[1], end=" ")
#     al += size[i]

# print(al)


'''
대문자 A ~ Z 가 저장된 list를 생성하는 코드를 작성
'''
# text = list()
# for v in range(ord("A"), ord("Z")+1):
#     text.append(chr(v))
# print(text)




'''
1~100 사이의 랜덤값 10개가 저장된 list를 작성

'''

lstA = list(range(10))

for i in range(10):
    lstA[i] = randint(1, 100)
    
print(lstA)
