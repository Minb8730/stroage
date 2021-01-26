# http:// 제외
# 처음 만나는 점 이후 부분은 제외
# 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!" 로 구성


# http://facebook.com

url = "http://facebook.com"
url_str = url.replace("http://","")
# print(url_str)

url_str = url_str[:url_str.index(".")]
# print(url_str)
password = url_str[:3] + str(len(url_str)) + str(url_str.count("e")) + "!"
print(password)

print("{}사이트의 비밀번호는 {}입니다.".format(url, password))


# print("{} 사이트의 비밀번호는 {} 입니다.".format(url, password))

