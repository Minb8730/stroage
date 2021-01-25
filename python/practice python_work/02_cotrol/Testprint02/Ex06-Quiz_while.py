'''
입력에 0이 들어올 때 까지의 합을 구하는 코드를 작성

'''
codeRun = True
numA = int(input("숫자 입력 >"))
sum = 0

while codeRun == True:
    numA = int(input("숫자 입력 >"))
    if numA != 0 :
        sum += numA
        print("이전까지 숫자의 총 합은 {} 입니다.".format(sum))
    else :
        codeRun = False





'''
1 이상의 숫자 3개의 합을 구하는 코드를 작성
- 3개의 값은 모두 저장하지 않아도 되고, -(마이너스) 값은 사용 할 수 없음
'''

num1 = int(input("번호 입력 1 : "))
num2 = int(input("번호 입력 2 : "))
num3 = int(input("번호 입력 3 : "))
sum2 = num1 + num2 + num3

if num1 or num2 or num3 < 1 :
    print("마이너스 값 혹은 1은 사용할 수 없습니다.")
else :
    print("{} + {} + {} = {}".format(num1, num2, num3, sum2))


'''
이름, 나이, 성별을 입력받아서 출력하는 코드를 작성
- 나이는 0~ 130 사이만 가능
- 성별은 남성, 여성만 가능
'''

name = input("이름을 입력하세요 >")
age = input("나이을 입력하세요 >")
gender = input("성별을 입력하세요 >")

if 0 < age or age > 130 :
    print("나이 값 입력의 오류입니다.")
if gender != "남성" or "여성" :
    print("성별을 정확하게 입력해 주세요.")

print("이름 : {}, 나이 : {}, 성별 : {}".format(name, age, gender))

'''
치즈 10Box 가 있는 창고에 암수 1쌍의 쥐가 살고 있습니다.
쥐 한마리가 하루에 먹을 수 있는 치즈의 양은 20g 이고, 치즈를 먹은 10일마다 쥐의 수가 2배씩 증가
몇일만에 창고의 치즈가 모드 없어지고, 이때까지의 쥐는 모두 몇 마리인지를 구하는 코드를 작성
- 치즈 1Box : 1kg

'''


