'''
아래의 문자열에서 소문자는 대문자로 변환
'''
str = "Never eVer giVe-up"
print(str.upper())



'''
아래의 주민등록번호에서 년월일 부분을 따로 분리해서 출력하는 코드를 작성

남성, 여성을 확인해주세요.
- 뒤에 일곱자리 중에서 첫번째 자리로 구분합니다.
    > 1,3 : 남성,   2,4 : 여성
'''
passport = "210104-1234567"

year = passport[:2]
month = passport[2:4]
day = passport[4:6]
gender = 0
if passport[-7] == 1 or 3:
    gender = "남성"
else:
    gender = "여성"
print("{}년 {}월 {}일 출생 {}입니다.".format(year, month, day, gender))


'''
생성하려는 ID, PW 가 정상인지를 확인하는 코드를 작성
- 아이디는 2자리이상 10자리까지 가능
- PW에는 아이디가 있으면 안됩니다.
'''

makeId = True

while makeId:
    ID = input("ID를 입력하세요 > ")
    if 2 <= len(ID) <= 10:
        print("사용 가능한 ID입니다.")
        makeId = False
    else:
        print("2자리 이상 10자리 미만의 아이디를 사용해 주세요.")


makePw = True
while makePw:
    PW = input("PW를 입력해 주세요 > ")
    if ID.find(PW) != -1:
        print("PW에는 ID를 포함할 수 없습니다.")
    else:
        print("사용 가능한 PW 입니다.")
        makePw = False        
'''
입력값이 알파벳 형태로만 되어 있어야 정상으로 처리하는 코드를 작성
'''

makeSen = True

while makeSen:
    onlyAlpha = input("알파벳으로 기입해주세요 > ")
    if onlyAlpha.isalpha() == True:
        print(onlyAlpha)
        makeId = False
    else:
        print("알파벳으로만 기입해주세요.")








