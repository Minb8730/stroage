
# 세 과목의 점수를 확인해서 합격 여부를 알려주는 코드를 작성
# - 합격 조건 : 과목별 점수가 40 이상이면서, 평균이 60 이상이어야 함

'''
class1 = int(input())
class2 = int(input())
class3 = int(input())

if class1 >= 40 and class2 >= 40 and class3 >= 40 and (class1 + class2 + class3) / 3 >= 60 :
    print("합격")
else:
    print("불합격")
'''





# 로그인 확인 코드를 작성
# - 로그인 확인시 사용 할 ID , PW를 설정해 놓습니다.
# - ID, PW 를 입력받아서 저장된 ID, PW 와 비교해서 로그인 기능 여부를 알려줍니다.

'''
id = str("minb8730")
pw = str(123456)

idcheck = str(input())
pwcheck = str(input())

if id == idcheck and pw == pwcheck:
    print("{} 아이디로 로그인 합니다.".format(id))
else :
    print("ID와 PW를 다시 한번 확인 해 주세요.")
'''

# ATM 코드를 작성
# - 통장 잔액을 알려줌
# 출금하려는 금액을 입력 받음
# 출금에 성공하면 출금 후 남은 잔액을 알려줌
# >  출금 조건 : 10000원 단위만 가능
# 인출 금액은 잔액보다 크면 안됨

account = 0
transfer = int(input())
account += transfer 
print("잔액은 {} 원 입니다.".format(account))

withdraw = int(input())
if withdraw % 10000 == 0 and account >= withdraw :
    account -=withdraw 
    print("{} 원을 인출 하였습니다.\n{} 원의 잔액이 남았습니다.".format(withdraw, account))

else :
    print("10,000원 단위만 인출 가능합니다.")






