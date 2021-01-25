from random import random, randrange, randint

'''
1 ~ 100 사이의 랜덤값 5개를 출력하는 코드를 작성
'''

# for cnt in range(5) :
#     ra = randint(1, 100)
#     print(ra)
    
'''
1.0 ~ 10.0 미만 사이의 랜덤값 5개를  출력하는 코드를 작성
'''

# for la in range(5):
#     rb = randomint(10, 100) / 10
#     print(rb)

'''
사용자 확인값을 생성하는 코드를 작성
- 사용자 확인값 : 0 ~ 9, A ~ Z 의 조합 5개
    Ex) J5G2Y, PIHGP, 23461
'''

# userCode = ""
# for cnt in range(5) :
#     select = randint(1, 2) #1 :0 ~ 9, 0: A ~ Z
#     data = ""
#     if select == 1 :
#         data = chr( randint(ord('0'), ord('9')))
#     else:
#         data = chr( randint(ord("A"), ord("Z")))
#     userCode += data
# print(userCode)


'''
UpDown 게임을 구현
- 1 ~ 100 사이의 랜덤값 하나를 컴퓨터에게 부여
 사용자에게 값을 입력받아서 컴퓨터가 가진값을 맞추면 됨
  > [  UP  ] : 입력한 값이 컴퓨터가 가진 값보다 낮을 때
    [  DOWN  ] : 입력한 값이 컴퓨터가 가진 값보다 높을 때
    [  정답  ] : 입력한 값이 컴퓨터가 가진 값보다 같을 때
  
'''

# com = randint(1, 100)
# count = 0

# gameRun = True
# while gameRun:
#     count += 1
#     user = int(input("{}번째 입력 > ".format(count)))

#     if user > com :
#         print("[  DOWN   ]")
#     elif user < com :
#         print("[  UP   ]")
#     else :
#         gameRun = False
# else:
#     print("[    정답    ]")
#     print("시도 횟수 : ", count)


'''
가위 바위 보 게임
- 컴퓨터에게 가위, 바위, 보 값 하나를 부여
  사용자에게 가위, 바위, 보 값을 입력받아서 결과 (승, 무, 패)를 알려주세요
- 3승 or 3패하면 실행을 멈추고 결과(승무패) 를 알려줍니다.
'''

# win = 0
# draw = 0
# lose = 0

# win_num, draw_num, lose_num = 0, 0, 0


# user = int(input("1.가위 2.바위 3.보 > "))

# while win < 2 and lose < 2:
#     win, draw, lose = 0, 0, 0 # 한 게임 초기화
#     com = randint(1,3)

#     if user >= 1 and user <= 3 :
#         if user == 1 :
#             if com == 1:
#                 draw = 1
#             elif com == 2:
#                 lose = 1
#             else :
#                 win = 1
#         if user == 2 :
#             if com == 2:
#                 draw = 1
#             elif com == 1:
#                 lose = 1
#             else :
#                 win = 1
#         if user == 3 :
#             if com == 3:
#                 draw = 1
#             elif com == 2:
#                 lose = 1
#             else :
#                 win = 1


#     if win == 1:
#         print("승리")
#     elif lose == 1:
#         print("패배")
#     else:
#         print("무승부")
    
'''
수학 문제 프로그램 
1. 덧셈 3문제를 내는 코드를 작성하세요 (자릿수 : 1~9)
   > 1문제가 나오면, 답을 입력해서 맞추면 됨
   > 문제가 끝나면 정답수를 알려줍니다.

2. 3문제가 끝나고 나면 다음 단계 진행을 확인
    다음 단계를 선택하면 문제의 자릿수가 증가 (자리수 : 1 ~ 99)
'''


rightanswer = 0
cnt = 0
QuizRun = True
while QuizRun:
    for cnt in range(1, 4) :
        numA = randint(1, 10)
        numB = randint(1, 10)
        answer = numA+numB
    
    
        print("{}번 문제 : {} + {} = ".format(cnt, numA, numB))
        user = int(input("정답은? "))
        if user == answer:
            print("정답")
            rightanswer += 1
        else:
            print("오답")

    print("정답 수 : ", rightanswer)
    print("다음 단계로 진행하시겠습니까?")
    
    comment = input("Y / N -> ")
    if comment == "Y":
        for cnt in range(1, 4) :
            numP = randint(1, 100)
            numO = randint(1, 100)
            answer2 = numP+numO
    
            print("{}번 문제 : {} + {} = ".format(cnt, numP, numO))
            user2 = int(input("정답은? "))
            if user2 == answer:
                print("정답")
                rightanswer += 1
            else:
                print("오답")
        print("정답 수 : ", rightanswer)
        break

    elif comment == "N":
        break

    else:
        print("Y/N 중에 선택해 주세요.")