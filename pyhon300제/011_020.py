#011
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsungstock = "삼성전자"
samsungstock_prise = 50000
print("{} 주식의 10주의 총 평가금액은 {} 원 입니다.".format(samsungstock, samsungstock_prise*10))

#012
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.

# 항목	값
# 시가총액	298조
# 현재가	50,000원
# PER	15.79

#013
# >> s = "hello"
# >> t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.

# 실행 예:
# hello! python

s = "hello"
t = "python"

print(s+"!",t)

#014
# 아래 코드의 실행 결과를 예상해보세요.

# >> 2 + 2 * 3 

# ->8


#015
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.

# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.

# >> a = "132"

a= 132
print(type(a))

#016
# 문자열 '720'를 정수형으로 변환해보세요.

# >> num_str = "720"

num_str = "720"
num_str = int(num_str)
print(type(num_str))


#017
# 정수 100을 문자열 '100'으로 변환해보세요.

# num = 100

num = 100
num = str(num)
print(type(num))

#018
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

fnum = "15.79"
fnum = float(fnum)
print(type(fnum))


#019
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.

# year = "2020"

year = "2020"
year = int(year)
print(year)
print(year-1)
print(year-2)


#020
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

month_pay = 48584
whole_month = 36
aircon = month_pay * whole_month
print(aircon)





