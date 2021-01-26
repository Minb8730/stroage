try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] /nums[1]))
    print("{0} /{1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 0으로 나눌수 없기 때문에 다시 예외처리 해야함
    print(err)
except: #nums.append(int(nums[0] /nums[1])) 나 모든 에러 값에 대해 예외처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


#사용자 정의 예외처리

class BignumberError(Exception) :
    def __str__(self, msg):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BignumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BignumberError as err :
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
    # 예외처리 구문에서 정상적으로 수행이 되건 오류가 발생하던 상관없이 무조건 실행