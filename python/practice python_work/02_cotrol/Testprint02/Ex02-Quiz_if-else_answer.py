

# Ex02-Quiz_if-else.py

'''
세과목의 점수를 확인해서 합격 여부를 알려주는 코드를 작성하세요
- 합격 조건 : 과목별 점수가 40이상이면서, 평균이 60이상이어야 합니다
'''
# s1 = int(input("첫번째 점수 입력 > "))
# s2 = int(input("두번째 점수 입력 > "))
# s3 = int(input("세번째 점수 입력 > "))
# print()

# sum = s1 + s2 + s3
# avg = sum / 3
# print("평균 : {:.1f}".format(avg))
# if s1 >= 40 and s2 >= 40 and s3 >= 40 and avg >= 60:
#     print("합격 ^^")
# else :
#     print("불합격 ㅠㅠ")



'''
로그인 확인 코드를 작성하세요
- 로그인 확인시 사용 할 ID, PW를 설정해 놓습니다
  ID, PW를 입력받아서 저장된 ID, PW 와 비교해서 로그인 가능 여부를 알려줍니다
'''
# sid = "test"
# spw = "1234"
# userid = input("ID 입력 > ")
# userpw = input("PW 입력 > ")
# print()
# if sid == userid and spw == userpw:
#     print("{}님이 로그인 하셨습니다..^^".format(userid))
# else :
#     print("ID or PW 오류")



'''
ATM 코드를 작성하세요
- 통장 잔액을 알려줍니다
  출금하려는 금액을 입력받습니다
  출금에 성공하면 출금 후 남은 잔액을 알려줍니다
  > 출금 조건 : 10000원 단위만 가능합니다 ( 10001 X )
               인출 금액은 잔액보다 크면 안됩니다
'''
balance = 100000
print("잔액 : {} 원".format(balance))

money = int(input("인출 금액 입력 > "))
print()

# balance -= money
if money > 0 and money % 10000 == 0 and money <= balance:
    # balance -= money
    # print("{} 원 출금 성공".format(money))
    # print("출금 후 잔액 : {} 원".format(balance))

    print("{} 원 출금 성공".format(money))
    print("출금 후 잔액 : {} 원".format(balance - money))
else :
    print("인출 금액 오류~")
print("잔액 : {} 원".format(balance))































