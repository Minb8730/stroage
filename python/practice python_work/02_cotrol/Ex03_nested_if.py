'''
중첩 if
- if 조건신_a :
     조건식_a가 참이면 실행
     if 조건식_b :
         조건식_a, 조거식_b 둘다 참이면 실행
     else :
         조건식_a 참, 조건식_b가 거짓이면 실행

> 첫번째 조건식을 만족했을 때, 그 결과를 재분류 또는 세분화 할 때 사용한다.

'''
'''
sid = "test"
spw = "1234"
userid = "test"
userpw = "1234"

if sid == userid and spw == userpw :
    print("{}님이 로그인 하였습니다.".format(sid))
else:
    if sid != userid :
        pinrt("ID 오류")
    else :
        print("PW 오류")

'''

data = 10
print("data :", data)
print()

if data >= 0:
    print("plus -", end="")
    if data % 2 == 1:
        print("홀수")
    else :
        print("짝수")
else :
    print("minus -", end="")
    if data % 2 == 1:
        print("홀수")
    else :
        print("짝수")