'''
리스트( list )
- list 를 생성 할 때에는 [] 를 사용
- list는 데이터의 수정이 가능하기 때문에 비어있는 리스트를 생성 할 수 있음
'''
'''
리스트 생성
'''

# a_ls = [1 ,2 ,3 ,4 ,5 ]
# print("a_ls : ", a_ls)
# print()

# b_ls = ['a', 1, '하나']
# print("b_ls : ", b_ls)
# print()

# c_ls = []
# print("c_ls : ", c_ls)
# print()

# d_ls = list() # 리스트 생성자
# print("d_ls : ", d_ls)
# print()

# e_ls = list(range(3))
# print("e_ls : ", e_ls)
# print()


# tmp = 1, 2, 3
# print("tmp : ", tmp)
# f_ls = list(tmp)
# print("f_ls : ", f_ls)
# print()



'''
index 사용
'''
# ls_1 = list(range(1, 6))
# print("ls_1 : ", ls_1)
# print("ls_1[3] : ", ls_1[3])
# print()

# # index 를 사용해서 요소의 값을 수정 할 수 있음
# ls_1[2] = 7
# print("ls_1 : ", ls_1)


'''
슬라이싱
'''

# ls_2 = ['a', 'b', 'c', 'd']
# print("ls_2 : ", ls_2)
# print("ls_2[1:3] : ", ls_2[1:3])

'''
list 연산
'''

# ls_3 = list(range(3))
# ls_4 = list(range(11, 15))
# print("ls_3 : ", ls_3)
# print("ls_4 : ", ls_4)
# print()

# ls_all = ls_3 + ls_4
# print("ls_all : ", ls_all)

'''----------------------------------------------------------------'''
# data = list(range(1, 6))
# print("data : ", data)
# print()

# '''
# append( value )
# - 리스트의 마지막에 value 요소를 추가
# '''
# data.append(99)
# print("data : ", data)
# print()

# '''
# insert ( index, value )
# -리스트의 index 위치에 value 요소를 추가
# '''

# data.insert(2, 77)
# print("data : ", data)

# '''
# remove( value )
# - 리스트에서 첫번째로 나오는 value 요소를 삭제 # 중복된 값이 존재하면 첫번째 value
# '''

# data.remove(77)
# print(("data : ", data))


'''
pop( index )
- 리스트의 마지막 or index 위치의 요소를 빼내오면서 삭제
'''
data = list(range(1, 6))
print("data : ", data)
print()

# data.pop()
# print("data : ", data)

# delete = data.pop(2)
# print("삭제 값 :", delete)
# print("data : ", data)

'''
index( value )
- 리스트 안에 value 요소가 있으면 그 위치값을 반환
'''
# sidx = data.index(3)
# print("3 위치 : ", sidx)

'''
count( value )
- 리스트 안에 value 요소가 몇개 있는지를 확인
'''

# cnt = data.count(2)
# print("{} 개수 : {}".format(2, cnt))


'''
reverse()
- 리스트의 요소를 역순으로 재배열
'''

# data.reverse()
# print("data : ", data)

'''
extend( list )
-list 안에 list를 추가
'''

# sub = [111, 222]
# data.extend(sub)
# print("data : ", data)

'''
clear()
- list 안의 모든 값을 삭제
'''

data.clear()
print("data : ", data)

'''
del()
- 프로그램에서 객체를 삭제
 > 객체를 삭제하기 때문에, del() 함수 이후에 객체를 사용하면 Error
'''

del(data)
print("data : ", data)