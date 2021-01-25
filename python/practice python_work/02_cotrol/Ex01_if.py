'''
제어문
- 위에서 아래로 순차적으로 실행되는 프로그램의 흐름을 변경 할 떄 사용
- 제어문에  포함되는 코드는 들여쓰기를 사용해서 작성

조건식
- 제어문의 실행 여부를 판단 할 때 사용
- 조건식의 마지막에는 ' :(콜론)' 을 작성
'''


'''
if문
- if 조건식 :
    조건식이 참이면 실행

 > if문 뒤에 조건식이 참이면 if문 안의 코드를 실행하고, 하위 코드를 진행
   if문 뒤에 조건식이 거짓이면 if문 안의 코드를 건너띄고 하위코드를 진행
'''
'''
data = 10
if data>= 0:
    print("plus")
print("- end -")

money = 2000

if money >= 2500:
    print("떡볶이 먹기")  #조건식이 거짓이기 떄문에 실행되지 않음
print("집으로 go")

money = 3000

if money >= 2500:
    print("떡볶이 먹기")
    money -= 2500
print("보유굼액 :", money)
'''

'''
value = int(input("숫자 입력 > "))
print()

if value % 2 == 1:
    print("홀수")
if value % 2 == 0:
    print("짝수")
if value > 0 and value < 11:
    print("1 ~ 10")
'''

word = "merry christmas"
print(word)

search = input("검색 문자 입력 > ")
print()
if search in word :
    print("success!")
if search not in word :
    print("fail")
    





