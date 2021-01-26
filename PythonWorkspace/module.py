#같은 경로에 있거나 혹은 파이썬 라이브러리가 있는 폴더에 있어야한다.

# import module_theater
# module_theater.price(3) # 3명이서 영화 보러 갔을 때 가격
# module_theater.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 떄
# module_theater.price_soldier(5) # 5명의 군인이 영화 보러 갔을 떄

# import module_theater as mv #모듈 이름을 다르게 호출할 수 있게 하는 명령어
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from module_theater import * #모듈을 따로 호출하지 않고 함수를 바로 불러올 수 있음
# price(3)
# price_morning(4)
# price_soldier(5)

# from module_theater import price, price_morning # 명시적으로 내가 필요한 함수만 가져와서 사용할 수 있음
# price(5)
# price_morning(4)
# price_soldier(5) # price_soldier 는 호출하지 않았기 때문에 에러가

from module_theater import price_soldier as discount
discount(5)