'''
함수( definition, function )
    - 하나 이상의 코드를 하나로 묶어서 만든 작은 프로그램.

함수 종류
- 내장 함수( built-in 함수 )
    > print(), input() .......
- python 라이브러리 함수
    > from ... import ...
- 사용자 정의 함수
    > 프로그래머가 필요에 의해서 직접 정의한 함수

함수 정의
- 'def' 키워드를 사용하여 하나 이상의 코드를 묶어서 거기에 이름을 붙여 놓은 것을 말함.
- 함수는 정의를 먼저하고, 정의된 함수를 호출해서 사용
    Ex) def 함수명 ( 매개변수 O,X ):
            실행코드
            return 값 ( O, X )
        >함수명 : 함수 호출(실행)시에 사용하는 이름
         매개변수 : 호출 지역에서 보내진 값을 보관하는 변수
         return : 함수 실행후에 나온 결과를 호출부로 보낼 때 사용

함수 호출
- 함수 이름을 사용해서 해당 함수의 코드를 실행
- 함수 실행에 필요한 값을 () 안에 작성해서 함수 정의부로 보낼 수 있습니다.
    Ex) 함수명 ( 인자값 O, X )
'''

'''
매개변수가 없는 함수
'''
# def hi():
#     print("안녕하세요~")

# hi()



'''
매개변수가 있는 함수
- 함수 정의부의 ()안에 변수가 있으면, 호출시에 값을 보내주어야 합니다.
    > 인자값과 매개변수의 개수는 일치해야 합니다.

'''
# def dataSend( arg ) :
#     print("받은 값 :", arg)

# dataSend("데이터 전송")
# dataSend(123)

'''
반환값이 있는 함수
- return 을 사용하면 함수 실행시에 나온 결과 하나를 호출부로 보낼 수 있습니다.
'''
# #변수에 저장하던지 다이렉트로 출력해야 값이 산출된다.
# def pi() :
#     return 3.141592
# pi() # 아무것도 출력되지 않음
# print(pi())
# rpi = pi()
# print("원주율 :", rpi)

'''
매개변수, 반환값 둘다 있는 경우
'''
def sendReceive( data ):
    print("받은 데이터 :", data)
    data = "response"
    return data

print(sendReceive("request"))
print()

'''-----------------------------------------------------------------------------'''

'''
전역변수
- 프로그램의 어디에서나 사용이 가능한 변수

지역변수
- 특정 지역안에서만 사용이 가능한 변수
해당 지역을 벗어나면 사용이 불가능
지역이 다르면 이름이 같아도 다른 변수

'''
# def tsetLocal_A():
#     a = 10
#     print("Local_A :", a)

# def tsetLocal_B():
#     a = 20
#     print("Local_B :", a)

# tsetLocal_A()
# tsetLocal_B()

'''
지역변수 사용 범위
'''
# def localData():
#     nation = "한국"
#     print("국가명 :", nation)

# nation = "kor"
# print("nation :", nation)
# localData()
# print("nation :", nation)


'''
전역 변수
'''
# def allData():
#     print("g :", g)

# g = 100
# allData()


# man = 0
# print("man :", man)

# def changeManA(data):
#     man = data

# changeManA(5)
# print("man :", man)

'''
전역변수를 함수 안에서 사용하려면 'global' 키워드를 붙여서 전역변수 사용을 선언해야 한다.
'''
man = 0
print("man :", man)

def changeManA(data):
    man = data

changeManA(5)
print("man :", man)

def changeManB(data):
    global man
    man = data

def changeMan(man, alterMan):
    man += alterMan
    return man

changeManB(10)
print("man :", man)

man = changeMan(man, 7)
print("man :", man)

'''-------------------------------------------------------------------------'''


'''
함수 실행주에 return 문이 실행되면 해당 위치에서 함수의 실행을 몸추고 호출위치로 돌아감
'''
# def monthCheck( month ):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         print("31일")
#         return
#     elif month in [4, 6, 9, 11]:
#         print("30일")
#     elif month == 2:
#         print("28일 or 29일")
#     else :
#         print("확인불가")
#     print("- End - ")

# month = 1
# monthCheck(month)



'''-------------------------------------------------------------------------'''

def inputIn():
    return int(input("숫자 입력 > "))

def oddCheck(data):
    if data % 2 == 1:
        return True
    return False


def oddData():
    data = inputIn()
    if oddCheck(data):
        print(data, " : 홀수")


value = inputIn()
print("입력 값 :", value)
print()
oddData()