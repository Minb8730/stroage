'''
input()
-키보드로 입력한 값을 프로그램에 저장 -> 터미널에서 직접 입력
'''

# va = input()
# print("va :", va)

# print("데이터 입력 > ", end="")
# va = input()
# print("va : ", va)


'''
input 함수 () 안에 출력 할 내용을 작성 할 수 있음
'''
# vb = input("키보드 입력 >")
# print("vb :", vb)


'''
input() 함수로 입력한 데이터는 모두 문자열str로 처리
'''
# vc = input("입력 > ")
# print("vc :", vc)
# print("vc type :", type(vc))


'''
input() 함수로 입력받은 값을 원하는 형태의 자료형으로 사용하고 싶으면, 형변환을 적용
'''

# dataA = input("숫자 입력_1 > ")
# dataB = input("숫자 입력_2 > ")
# result = dataA + dataB #문자열이기 때문에 그냥 이어진 값으로 ex) A: 3 B:2 인 경우 32로 출력 
# print("result :", result)

# dataA= int(dataA)
# dataB= int(dataB)
# result = dataA + dataB # int로 변환했기 때문에 5로 출력
# print("result :", result)

# ia = int(input("첫번째 숫자 입력 > "))
# ib = int(input("두번째 숫자 입력 > "))
# res = ia + ib
# print("{} + {} = {}".format(ia, ib, res))  


# nation = "한국 kor" # split 이라고 띄어쓰기(공백) 을 기준으로 값을 분리시켜 줄수 있음
# n1,n2 = nation.split()
# print("n1 : {} - n2 : {}".format(n1, n2))

data = input("데이터 두개 입력 >")
print("data :", data)

d1, d2 = data.split()
print("d1 : {} - d2 : {}".format(d1, d2) )

