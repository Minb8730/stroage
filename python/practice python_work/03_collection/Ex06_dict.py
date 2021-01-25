'''
dict( 딕셔너리 )
- 딕셔너리는 'key(키) : value(값)' 을 한쌍으로 대응시켜서 구현한 컬렉션
 > 다른 언어에서는 'map' 이라고 한다.
- 딕셔너리는 {}사용해서 선언하고, 하나의 요소는 'key:value' 로 이루어 진다.
 > key  :수정불가 - 정수, 문자열   
   value : 수정가능
-key 값은 중복될 수 없으며, 하나의 key에 하나의 value 가 연결
-key 값을 사용해서 딕셔너리 안의 요소를 사용
'''

# d1 = {}
# print("d1 :", d1)
# print("d1 type :", type(d1))
# print()

# d2 = dict()
# print("d2 :", d2)
# print("d2 type :", type(d2))
# print()

# d3 = { 1:"one", 2:"two", 3:"three"}
# print("d3 :", d3)
# print()

# d4 = { "루피":11, "조로":10, "초파":7}
# print("d4 :", d4)
# print()

# son = {"이름":"손흥민", "소속":"토트넘", "나이":29}
# print("son :", son)

# 딕셔너리 안에 중복된 key가 있으면 마지막에 선언된 key가 적용
# d5 = { "a":1, "b":2, "a":7}
# print("d5 :", d5)

# member = [("memA", 20), ("memB", 30), ("memC", 33)]
# print("member :", member)
# print()

# member_dict = dict(member)
# print("member_dict :", member_dict)

# d6 = dict( 고객_a = 20, 고객_b = 27)
# print("d6 :", d6)


'''------------------------------------------------------------------------------------'''

'''
dict 요소 사용
-dict명 ( key )
  > 요소에 접근 할 때 사용하는 key 값으로 변수를 적용 할 수 있음.
  > 없는 key 를 사용하면 error 

'''
# sports = dict( 손흥민 = 29, 추신수 = 39, 류현진 = 35)
# print(sports)
# print()

# print("손흥민 나이 :", sports["손흥민"])
# print()

# search = "추신수"
# print("추신수 나이 :", sports[search])
# print()

# sports["류현진"] = 33
# print("sports :", sports)
# print()

# print("유재석 나이 :", sports["유재석"]) #Error
# 없는 key 값을 수정하려고 하면, 해당 내용이 error

# sports["유재석"] = 48
# print("sports : ",sports)

'''-----------------------------------------------------------'''

man = dict( 손흥민 = 29, 추신수 = 39, 유재석 = 48)
print(man)

'''
dict명.keys()
- 딕셔너리 안의 key 만을 모아서 tuple 로 만들어 dict_keys 로 반환
'''
# man_k = man.keys()
# print("man key :", man_k)

# for k in man_k:
#     print(k)
# print()

# key_ls = list(man_k)
# print("key_ls :", key_ls)
# print()


'''
dict.values()
- 딕셔너리안의 value 만을 모아서 tuple로 만들어서 dict_values로 반환
'''
# man_v = man.values()
# print("man value :", man_v)
# print()

# for v in man_v:
#     print(v)
# print()


'''
dict명.items()
- 딕셔너리 안의 'key:value' 를 tuple로 만들어서 dict_item로 반환
'''
# man_items = man.items()
# print("man_itme :", man_items)
# print()

# for it in man_items:
#       k, v = it
#       print(k , v)
# print()


'''
dict명.get( key, "default value" )
-key 값을 사용해서 해당 value 를 반환
-key 값이 없으면 Error 가 나지 않고 'None' 값을 반환
'''
# print("추신수 나이 :", man.get("추신수"))
# print("박명수 나이 :", man.get("박명수"))
# print("박찬호 나이 :", man.get("박찬호", "없는 이름입니다."))


'''
dict명.setdefault( key, value)
-하나의 요소를 추가 할 때 사용
-key 값이 없으면 추가되고, key 값이 있으면 변경되거나 추가되지 않음

'''
# man.setdefault("박찬호")
# print(man)
# man.setdefault("손흥민", 50)
# print(man)


'''
dict명.update( { key : value })
dict명.update( dict )
> 딕셔너리에 여러개의 요소를 추가하거나 변경 할 수 있습니다.
  key 값이 있으면 value가 변경되고, key 값이 없으면 key:value를 추가
'''
# man.update({"박찬호":46})
# print(man)



'''
dict명.pop( key )
- key를 사용해서 요소를 삭제
  > key 값이 없으면 error 
'''
# man.pop("손흥민")
# print(man)

'''
dict명.popitem()
- 딕셔너릴 안에 저장된 데이터 순서대로 한개의 요소를 tuple로 반환해서 삭제

'''
# popdata = man.popitem()
# print("삭제 데이터 :", popdata)
# print()
# dk, dv = popdata
# print("삭제 key : {} - value : {}".format(dk, dv))
# print()

'''
dict명.clear()
- 딕셔너리 안의 모든 요소를 삭제
'''
man.clear()
print(man)


'''
{}.fromkeys( tuple or list )
- tuple, list 의 요소를 key 값으로 사용해서 새로운 dict를 생성
'''
# num = list(range(1, 6))
# print("num :", num)
# num_dic = {}.fromkeys(num)
# print("num_dic :", num_dic)
# print()

# num2_dic = {}.fromkeys(num, "n/a")
# print("num2_dic :", num2_dic)


'''-----------------------------------------------------------'''

'''
in, not in 연산자를 사용해서 key값이 있는지를 확인 할 수 있음.
'''
# no_dic = dict( 일 = 1, 이 = 2, 삼 = 3)
# print("no_dic :", no_dic)
# print()

# search = "이"
# if search in no_dic:
#       print("success")
# else :
#       print("fail")


''' ---------------------------------------------------------------------'''

# site_dic = dict()

# urltitle = input("사이트명 입력 >")
# url = input("URL 입력 > ")
# print()

# site_dic.setdefault(urltitle, url)
# print(site_dic)


''' ---------------------------------------------------------------------'''


person = dict()
info = list()

name = "손흥민"
info = [ 29, "토트넘"]
person.setdefault(name, info)
print(person)
print()

el = person.get(name)
print("{} 정보".format(name))
print("나이 : {} 세".format(el[0]))
print("소속팀 :", el[1])
print()


name = "박찬호"
sk = ""
sv = ""
if name in person:
    for item in person.items():
        k, v = item
        if k == name:
            sk = k
            sv = v
    
    print("- {} 정보 -".format(name))
    print("나이 :", sv[0])
    print("소속팀 :", sv[1])

else:
    print("검색 실패~")





'''-----------------------------------------------------------'''
