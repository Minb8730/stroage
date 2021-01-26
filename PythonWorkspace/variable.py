'''
지역변수와 전역변수

지역변수는 함수 내에서만 사용 가능, 함수가 호출 될때 만들어 졌다가 함수 호출이 끝나면 사라짐

전역변수는 모든 공간에서, 프로그램 내에서 어디서든 부를 수 있는 변수
'''
'''
gun = 10 #총 10자루 -> 함수 밖의 변수

def checkpoint(soldiers) : #경계근무
    # gun = 20 #함수 내의 지역변수
    global gun # global로 전역 변수 값으로 함수 밖의 10자루 gun을 불러옴
    gun-= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명 경계 근무 나감
print("남은총 : {0}".format(gun))
'''


gun = 10
def checkpoint(soldiers) : #경계근무
    global gun # global로 전역 변수 값으로 함수 밖의 10자루 gun을 불러옴
    gun-= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers): #return
    gun-= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은총 : {0}".format(gun))
