'''
break 문
- 실행중인 반복문을 강제로 종료 시킬 때 사용
- 중첩된 반복문에서 break 문과 가까운 제어문 하나만 종료


'''

# value = 0
# while True :
#     if value == 10 :
#         break
#     value += 1
#     print(value)


# for v in range(1, 10) :
#     if v == 8:
#         break
#     print(v, end = " ")

    
# for line in range(1, 4) :
#     print("{} line : ".format(line), end= "")
#     for v in range(1, 10):
#         if v == 8:
#             break
#         print(v, end = " ")
#     print()
    
'''
continue 문
- 반복문 안에서 continue 문이 실행되면 현재 진행중인 반복문의 실행을 멈추고, 다음 반복을 진행

'''

# value = 0
# while value < 10:
#     value += 1
#     if value % 7 ==0:
#         print("jump")
#         continue
#     print(value)


# for v in range(1, 10):
#     if v % 7 == 0:
#         print("lucky")
#         continue
#     print(v)

'''
while else, for else
- 반복문이 정상적으로 끝까지 실행되면, else 문의 코드를 실행

'''

# textRun = True
# while textRun:
#     text = input(">>")
#     if text == "stop":
#         textRun = False
#         continue
#     print(text)
# else:
#     print("bye")


data = { 1, 9, 3, 5, 7}
for v in data:
    if v % 2 == 0:
        print("짝수")
        break
else :
    print("짝수가 없음")