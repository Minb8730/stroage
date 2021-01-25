'''
-while 조건식 :
    조건식이 참이면 실행

>조건식이 참인동안 반복문의 코드를 실행

'''

# line = 0
# while line < 5 :
#     print("*" * 10)
#     line += 1

# data = 5
# while data: #0을 제외하면 참, 0이 되는 순간 거짓이기 때문에 조건문을 탈출
#     print(data)
#     data -= 1


# data = 0
# loop = True
# while loop :
#     data += 1
#     if data == 10: # 탈출 조건문
#         loop = False

# value = 0
# run = True
# while run :
#     value = int(input("1~10 사이의 수 입력 >"))
#     if value >= 1 and value <= 10:
#         run = False
# print("입력값 : ", value)

# print("- text 입력기 ( 정지 : stop ) -")
# text = ""
# while text != "stop" :
#     text = input(">> ")
#     if text != "stop" :
#         print(text)



data = ""
select = ""
codeRun = True
while codeRun :
    select = int(input("1.입력 2.출력 0.종료 >"))

    if select == 1:
        data = input("데이터 입력 >")

    elif select == 2 :
        print(data)
    elif select == 0 :
        codeRun = False
    else :
        print("선택 오류")

print("--------End----------")


