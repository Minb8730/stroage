

# Ex01-Quiz_module.py

from random import random, randrange, randint

'''
1 ~ 100 사이의 랜덤값 5개를 출력하는 코드를 작성하세요
'''
# for n in range(5):
#     v = randint(1, 100)
#     print(v, end=" ")
# print()


'''
1.0 ~ 10.0 미만 사이의 랜덤값 5개를 출력하는 코드를 작성하세요
'''
# for n in range(5):
#     v = randint(10, 100) / 10
#     print(v, end=" ")
# print()



'''
사용자 확인값을 생성하는 코드를 작성하세요
- 사용자 확인값 : 0 ~ 9, A ~ Z 의 조합 5개
  Ex) J5G2Y, PIHGP, 23461 
'''
# userCode = ""
# for cnt in range(5):
#     select = randint(1, 2)   # 1 : 0 ~ 9,  2 : A ~ Z
#     data = ""
#     if select == 1:
#         data = chr( randint(ord('0'), ord('9')))
#     else:
#         data = chr( randint(ord('A'), ord('Z')))
#     userCode += data
# print(userCode)
# print()



'''
UpDown 게임을 구현하세요
- 1 ~ 100 사이의 랜덤값 하나를 컴퓨터에게 부여합니다
  사용자에게 값을 입력받아서 컴퓨터가 가진값을 맞추면 됩니다
  > [  UP  ] : 입력한 값이 컴퓨터가 가진 값보다 낮을 때
    [ DOWN ] : 입력한 값이 컴퓨터가 가진 값보다 높을 때
    [ 정답 ] : 입력한 값이 컴퓨터가 가진 값이랑 같을 때
- 정답을 맞추면 이때까지의 시도 횟수를 알려줍니다
'''
# com = randint(1, 100)
# count = 0

# gameRun = True
# while gameRun:
#     count += 1
#     user = int(input("{}번째 입력 > ".format(count)))

#     if user > com:
#         print("[ DOWN ]")
#     elif user < com:
#         print("[  UP  ]")
#     else:
#         gameRun = False
# else:
#     print("정답!! ^^")
#     print("시도 횟수 :", count)



'''
가위, 바위, 보 게임
- 컴퓨터에게 가위, 바위, 보 값 하나를 부여합니다
  사용자에게 가위, 바위, 보 값을 입력받아서 결과(승, 무, 패)를 알려주세요 
- 3승 or 3패하면 실행을 멈추고 결과(승무패)를 알려줍니다
'''
# win = 0  # 승
# draw = 0 # 무
# lose = 0 # 패
# resWin, resDraw, resLose = 0, 0, 0 # 최종 결과

# # 1.가위  2.바위  3.보
# while resWin < 3 and resLose < 3:
#     win, draw, lose = 0, 0, 0  # 한게임 결과 초기화

#     com = randint(1, 3)
#     print("com :", com)
#     user = int(input("1.가위  2.바위  3.보 >> "))

#     if user >= 1 and user <= 3:
#         if user == 1:  # 가위
#             user = "가위"
#             if com == 1:
#                 draw = 1
#             elif com == 2:
#                 lose = 1
#             else:
#                 win = 1
#         elif user == 2: # 바위
#             user = "바위"
#             if com == 1:
#                 win = 1
#             elif com == 2:
#                 draw = 1
#             else:
#                 lose = 1
#         elif user == 3: # 보
#             user = "보"
#             if com == 1:
#                 lose = 1
#             elif com == 2:
#                 win = 1
#             else:
#                 draw = 1

#         # com 가위, 바위, 보 설정
#         if com == 1:
#             com = "가위"
#         elif com == 2:
#             com = "바위"
#         else:
#             com = "보"
        
#         print("user : {} -  com : {}".format(user, com))
        
#         # 한게임 결과
#         if win == 1:
#             print("승리")
#             resWin += 1
#         elif lose == 1:
#             print("패배")
#             resLose += 1
#         else:
#             print("무승부")
#             resDraw += 1

#     else:
#         print("선택 오류~")
#     print()

# else:
#     print("{}승 {}무 {}패".format(resWin, resDraw, resLose))


"""------------------------------------------------------------"""


'''
수학 문제 프로그램
1. 덧셈 3문제를 내는 코드를 작성하세요 ( 자릿수 : 1 ~ 9 )
   > 1문제가 나오면, 답을 입력해서 맞추면 됩니다
     3문제가 끝나면 정답수를 알려줍니다

2. 3문제가 끝나고 나면 다음 단계 진행을 확인합니다
   다음 단계를 선택하면 문제의 자릿수가 증가 합니다 ( 자리수 : 1 ~ 99 )
'''
rightAnswer = 0  # 정답수
limit = 10       # 자릿수

quizRun = True
while quizRun:
    for cnt in range(3):
        x, y = randint(1, limit-1), randint(1, limit-1)
        res = x + y
        print("{} + {} = ?".format(x, y))
        user = int(input("결과 입력 > "))
        if user == res:
            print("정답입니다~ ^^")
            rightAnswer += 1
        else:
            print("틀렸어요~ ㅠㅠ")
        print()
    
    print("정답수 :", rightAnswer)

    # 다음 단계 확인
    while True:
        next = int(input("다음 단계(1.yes  2.no) > "))
        if next == 1 or next == 0:
            if next == 1:
                print("다음 단계~")
                limit *= 10
            else:
                quizRun = False
            break
    print()

else:
    print("총 정답수 :", rightAnswer)












































