#021
# ㅣetters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.

# >> letters = 'python'
# 실행 예
# p t

letters = "python"
print(letters[0], letters[2])


#022
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.

# >> license_plate = "24가 2210"
# 실행 예: 2210

license_plate = "24가 2210"
print(license_plate[-4:])


#023
# 아래의 문자열에서 '홀' 만 출력하세요.

# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

string = "홀짝홀짝홀짝"
print(string[::2])


#024
# >> string = "PYTHON"
# 실행 예:
# NOHTYP

string2 = "PYTHON"
print(string2[::-1])

#025

# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.

# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222

phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))


#026
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.

# 실행 예
# 01011112222
print(phone_number.replace("-", ""))


#027
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.

# >> url = "http://sharebook.kr"
# 실행 예:
# kr
url = "http://sharebook.kr"
print(url[-2:])
url = url.split(".")
print(url[1])

#028
# 아래 코드의 실행 결과를 예상해보세요.

# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)

#029
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A

string = 'abcdfe2a354a32a'
print(string.replace("a", "A"))



#030
# 아래 코드의 실행 결과를 예상해보세요.

# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)

# ->abcd