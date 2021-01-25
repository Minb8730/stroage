'''
모듈 (라이브러리)
- 비슷한 기능을 가진 함수, class 를 정의해 놓은 파일
- 모듈을 사용하기 위해서는 어떠한 모듈을 사용 할 것인지를 코드안에 작성해야 한다.

'''

'''
모듈과 모듈안의 함수를 이용하는 방법

import 모듈 이름
- 모듈안에 있는 함수를 사용 할 때에는 '.' 연산자를 사용
Ex) import 모듈명
    모듈명.함수
    모듈명.변수

import 모듈명 as 추가이름
- 기본 모듈명을 다른 이름으로 지정해서 사용 가능

from 모듈명 import 모듈함수
- 모듈안에 있는 특정 함수를 편리하게 사용 할 수 있음
'''

# import random
# print(random.random())

# import random as rd
# print(rd.random())

# from random import random
# print(random())


'''
random 모듈
-임의의 숫자를 자동으로 생성하는 기능을 가진 모듈
'''
from random import random
from random import randint
from random import randrange
'''
- 0.0 ~ 1.0 미만 사이의 실수를 생성하는 함수

'''
# ra = random()
# print(ra)

# rb = random() * 10 # 0.0 ~ 1.0 미만
# print(rb)

# rc = int(random() * 100)
# print(rc)

'''
randint( 시작, 종료 )
- 지정한 범위안의 정수를 생성합니다.

'''

# rd = randint(1, 3)
# print(rd)

# re = randint(50, 100)
# print(re)

# rf = randint( 65, 90)
# rf = chr(rf)
# print(rf)

# rg = chr( randint( ord("A"), ord("Z")))
# print(rg)



'''
randrange(시작, 종료, 증감)
'''
rh = randrange(1, 10) # 1~9
print(rh)

for cnt in range(10) :
    tmp = randrange(0, 11, 2)
    print(tmp, end = " ")
    






