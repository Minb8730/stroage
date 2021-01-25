'''
문자열
 - 문자 데이터 여러개의 집합입니다.

 print("python 문자열")
 
외따옴표 3개를 사용하면 여러줄의 문자열을 한번에 출력 할 수 있습니다.

 '''
 
print(''' 이런 식으로 적용
히면
가능합니다.''')

'''
문자열 연산
- 숫자처럼 문자열끼리 서로 더하거나 곱하는게 가능
'''

textA = "smile"
textB = "^^"
print("textA :", textA)
print("textB :", textB)

stn = textA + " " + textB
print(stn)

print(textA * 4)




'''
문자열은 문자들의 집합이기 때문에 특정위치의 문자를 선택하여 사용 할 수 있음.
 - 각 문자 위치에는 index(번호) 가 부여되어 있음.
 - index는 0부터 시작해서 1씩 증가함.
 Ex) 변수명[index]
 
 #+        01234 56 7 8
 nation = "korea대한민국"
 #-        98765 43 2 1
 '''
nation = "korea대한민국"
print("nation :", nation)
print("nation :", nation[0])
print("nation :", nation[6])
print("nation :", nation[-3])

