#271
#  은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
#  Account 클래스를 생성한 후 생성자를 구현해보세요.
#  생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.

# 은행이름: SC은행
# 계좌번호: 111-11-111111

from random import*

# class Account:
#     account_count = 0

#     def __init__(self, user_name, balance):
#         self.bank_name = "SC은행"
#         self.user_name = user_name
#         self.balance = balance
        
#         num1 = randint(0, 999)
#         num2 = randint(0, 99)
#         num3 = randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 + "-" + num2 + "-" + num3

#         Account.account_count += 1

# kim = Account("김민수", 100)
# print(kim.user_name)
# print(kim.balance)
# print(kim.bank_name)
# print(kim.account_number)


    # def account_number(self):
    #     # self.account_number = \
    #     for digit_start in range(3):
    #         digit_start = randint(0, 9)
    #         print(digit_start, end = "")
       
    #     print("-", end = "")
       
    #     for digit_middle in range(2):
    #         digit_middle = randint(0, 9)
    #         print(digit_middle, end = "")
       
    #     print("-", end = "")
       
    #     for digit_last in range(6):
    #         digit_last = randint(0, 9)
    #         print(digit_last, end = "")




#272
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

# kim = Account("김민수", 100)
# print(Account.account_count)
# lee = Account("이민수", 100)
# print(Account.account_count)



#273
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.

# class Account:
#     account_count = 0

#     def __init__(self, user_name, balance):
#         self.bank_name = "SC은행"
#         self.user_name = user_name
#         self.balance = balance
        
#         num1 = randint(0, 999)
#         num2 = randint(0, 99)
#         num3 = randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 + "-" + num2 + "-" + num3

#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):   # 객체로 부터 받을 필요가 없이 Class로부터 바로 받으면 되기 때문에 self 를 쓰지 않아도 된다.
#         print(cls.account_count)    # 하지만 인자를 받아야 하기 때문에 클래스 메소드를 사용해준다. 이를 통해 인자에 클래스 자체를 받는다.

    
# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# kim.get_account_num()



#274
# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

# class Account:
#     account_count = 0

#     def __init__(self, user_name, balance):
#         self.bank_name = "SC은행"
#         self.user_name = user_name
#         self.balance = balance
        
#         num1 = randint(0, 999)
#         num2 = randint(0, 99)
#         num3 = randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 + "-" + num2 + "-" + num3

#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):   
#         print(cls.account_count)

#     def deposit(self, input_money):
#         if balance > 0:
#             self.balance += input_money
#         else:
#             print("잘못된 입력")   


#275
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

# class Account:
#     account_count = 0

#     def __init__(self, user_name, balance):
#         self.bank_name = "SC은행"
#         self.user_name = user_name
#         self.balance = balance
        
#         num1 = randint(0, 999)
#         num2 = randint(0, 99)
#         num3 = randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 + "-" + num2 + "-" + num3

#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):   
#         print(cls.account_count)

#     def deposit(self, input_money):
#         if input_money > 0:
#             self.balance += input_money
#         else:
#             print("잘못된 입력")   

#     def withdraw(self, output_money):
#         if self.balance > output_money:
#             self.balance -= output_money
#         else:
#             print("출금금액이 잔액보다 큽니다.")


#276
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.

# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10,000원


# class Account:
#     account_count = 0

#     def __init__(self, user_name, balance):
#         self.bank_name = "SC은행"
#         self.user_name = user_name
#         self.balance = balance
        
#         num1 = randint(0, 999)
#         num2 = randint(0, 99)
#         num3 = randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 + "-" + num2 + "-" + num3

#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):   
#         print(cls.account_count)

#     def deposit(self, input_money):
#         self.deposit_count += 1
#         if input_money > 0:
#             self.balance += input_money
#         else:
#             print("잘못된 입력")   
#         if self.deposit_count % 5 == 0:
#             self.balance = self.balance *1.001


#     def withdraw(self, output_money):
#         if self.balance > output_money:
#             self.balance -= output_money
#         else:
#             print("출금금액이 잔액보다 큽니다.")

#     def display_info(self):
#         print("은행이름: {}\n예금주 : {}\n계좌번호 : {}\n잔고 : {:,}원".format(self.bank_name, self.user_name , self.account_number, self.balance))


    


# py = Account("파이썬",10000)
# py.display_info()



#277
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.


#278
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.

# data = []
# k = Account("KIM", 10000000)
# l = Account("LEE", 10000)
# p = Account("PARK", 10000)

# data.append(k)
# data.append(l)
# data.append(p)

# print(data)

#279
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

# for i in data:
#     if i.balance >= 1000000:
#         i.display_info()


#280
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

class Account:
    account_count = 0

    def __init__(self, user_name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.bank_name = "SC은행"
        self.user_name = user_name
        self.balance = balance
        
        num1 = randint(0, 999)
        num2 = randint(0, 99)
        num3 = randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):   
        print(cls.account_count)

    def deposit(self, input_money):
        self.deposit_count += 1
        if input_money > 0:
            self.balance += input_money
            self.deposit_log.append(input_money)

        else:
            print("잘못된 입력")   
        if self.deposit_count % 5 == 0:
            self.balance = self.balance *1.001


    def withdraw(self, output_money):
        if self.balance > output_money:
            self.balance -= output_money
            self.withdraw_log.append(output_money)

        else:
            print("출금금액이 잔액보다 큽니다.")

    def display_info(self):
        print("은행이름: {}\n예금주 : {}\n계좌번호 : {}\n잔고 : {:,}원".format(self.bank_name, self.user_name , self.account_number, self.balance))

    def deposit_history(self):
        for output_money in self.withdraw_log:
            print(output_money)

    def deposit_withdraw(self):
        for input_money in self.withdraw_log:
            print(input_money)

k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()








