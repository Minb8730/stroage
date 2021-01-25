'''
set
-중복이 없는 요소로 구성된 collection 
-set은 {} 를 사용하여 생성
-sequence, key 가 사용되지 않고 값만 저장되기 때문에 데이터가 있고, 없고만 알 수 있음.
'''

'''
set 생성
'''

# s1 = { 1, 2, 3}
# print("s1 :", s1)
# print()

# s2 = { 1, "일", "하나"}
# print("s2 :", s2)
# print()

# s3 = set()
# print("s3 :", s3)
# print()

# #set() 생성자를 사용해서 하나의 문자열을 저장하여 분리되어 set에 저장
# # - 중복된 문자가 있으면 하나만 저장

# s4 = set("word")
# print("s4 :", s4)
# print()

# s5 = set("google")
# print("s5 :", s5)
# print()


# no_ls = list(range(1,6))
# print("no_ls :", no_ls)
# print()

# no_set = set(no_ls)
# print("no_set :", no_set)
# print()

'''------------------------------------------------------------------------------'''
# ex = {1, 2, 3, 4, 5}
# print("ex :", ex)
# print()

'''
add( value )
- set 에 value 요소를 추가
'''
# ex.add(10)
# print("ex :", ex)
# print()

'''
update( list )
- 한번에 여러개의 요소를 추가
'''
# ex.update([7, 8, 9])
# print("ex :", ex)
# print()

'''
remove( value )
- set에서 value 요소를 삭제
- 삭제 값이 없으면 error 입니다.
'''

# ex.remove(5)
# print("ex :", ex)
# print()


'''
clear()
-set 의 전체 요소를 삭제
'''

# ex.clear()
# print("ex :", ex)

''' --------------------------------------------------------------------'''
'''
집합 연산
'''
dataA = {1, 2, 7, 3, 5}
dataB = {2, 5, 3}
# print("dataA :", dataA)
# print("dataB :", dataB)
# print()

# # 교집합
# i_data = dataA & dataB 
# print("교집합 :", i_data)
# i2_data = dataA.intersection(dataB)
# print("교집합 :", i2_data)
# print()

'''
합집합
'''
u_data = dataA | dataB 
print("u_data :", u_data)
u2_data = dataA.union(dataB)
print("u2_data :", u2_data)
print()

'''
차집합
'''
d_data = dataA - dataB 
print("d_data :", d_data)
d2_data = dataA.difference(dataB)
print("d2_data :", d2_data)
print()
