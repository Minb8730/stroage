# for n in range( 1,6 ) : # -> 를 3번 실행 시키는 것이 아니라 제어문을 통해서 출력 가능
#     print(n, end = " ")
# for n in range( 1,6 ) :
#     print(n, end = " ")
# for n in range( 1,6 ) :
#     print(n, end = " ")


# for out in range(3) : # 위와 출력이 같음
#     for n in range(1, 6):
#         print(n, end = " ")
#     print()

# for dan in range(2, 10):
#     print("- {} 단 -".format(dan))
#     for su in range(1, 10):
#         print("{} x {} = {}".format(dan, su, dan*su))
#     print()

select = 0
gameRun = True

while gameRun :
    for heart in range(3, 0, -1 ) :
        print("생명 :", heart)
    select = int(input("1. 재시작, 0. 종료 >"))
    if select == 0 :
        gameRun = False
print(" -Game end- ")
