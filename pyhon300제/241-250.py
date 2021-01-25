#241
import datetime
now = datetime.datetime.now()
print(now)

#242
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.

print(now, type(now))
print()

#243
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

now = datetime.datetime.now()

# 원하는 날짜를 출력
# delta = datetime.timedelta(days = num)
# print( now + delta)

# 원하는 시간을 출력
# delta = datetime.timedelta(hours = num)
# print( now + delta)

for day in range(5, 0, -1):
    delta = datetime.timedelta(days = day)
    date = now - delta
    print(date)

print()


#244
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# 18:35:01 

now = datetime.datetime.now()
a = now.strftime("%H:%M:%S")
print(a, type(a))


#245
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. 
# "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
print()
day = "2020-05-04"
tictok = datetime.datetime.strptime(day, "%Y-%m-%d")
print(tictok)


#246
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.

'''
# hello 를 출력 후 4초 뒤에 continue 를 출력
print("hello")
time.sleep(4)
print("continue")
'''
print()

import time

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)


#247
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
'''
import os               -> os.rename()
from os import rename   -> rename()
from os import*         -> getcwd(), rename(), ...
import os as my_os      -> my_os()
'''

#248
# os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
import os
res = os.getcwd()
print(res, type(res))


#249
# 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.




#250
# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.








