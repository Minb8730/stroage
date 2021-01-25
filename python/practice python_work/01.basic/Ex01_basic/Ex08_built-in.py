'''
내장함수(built-in 함수)
-python 프로그램에서 기본적으로 사용 할 수 있는 함수

'''

'''
round(value, 자리수)
- 소수점 값에 대해서 지정된 자리까지 반올림하는 기능을 가진 함수
'''

'''
v1 = round(12.1234, 2)
print("v1 :", v1)


v2 = 12.1234
print("v2 :", v2)
v2 = round(v2, 3)
print("v2 ", v2)
'''

'''
max()
- 데이터 목록에서 가장 큰 값을 찾는 기능을 가진 함수

min()
- 데이터 목록에서 가장 작은 값을 찾는 기능을 가진 함수

sum()
- 데이터 목록의 전체 합을 구하는 함수

'''
'''
data = [2, 1, 6, 5, 7]
print(data)

maxData = max(data)
print("큰값 :", maxData)

minData = min(data)
print("작은 값 :", minData)

dataSum = sum(data)
print("합 :", dataSum)
'''

'''
pow()
- 거듭제곱 값으로 구하는 함수
'''
'''
v3 = pow(2, 4)
print("2의 4승:", v3)
'''

'''
divmod()
- 나눗셈 한 결과의 몫과 나머지를 구하는 함수
'''
'''
d, m = divmod(10, 3)
print("10 / 3 --> 몫 : {}, 나머지 : {}".format(d, m))
'''

'''
abs()
- 절대갑을 구하는 함수
'''

'''
v6 = -7
print("v6 :", v6)

v6 = abs(v6)
print("v6 :", v6)
'''


'''
ASCII(아스키코드)
- 0 ~ 127 사이의 숫자들에게 각각 하나의 문자 or 기호를 대응시켜 정리해 놓은 문자변환 규약표

chr()
- 숫자를 문자로 변환하는 함수

ord()
- 아스키 코드의 문자값을 숫자로 변환하는 함수
'''
n1 = 65
print("n1 :", n1)

n1 = chr(n1)
print("n1 :", n1)

n2 = 'a'
print("n2 :", n2)
n2 = ord(n2)
print("n2 :", n2)

res = chr(ord(n1) + 32)
print(res)



