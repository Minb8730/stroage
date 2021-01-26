'''
score_file = open("score.txt", "w", encoding = "utf8") 
#open 으로 file을 열고 w(write) 쓰기위한 파일이라고 정의, 한글정보를 에러가 나지 않게 하기 위해 encoding = "utf8"
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close() # 닫아줘야한다.
'''
# -> 이 과정을 거치면 새로운 파일이 생성됨

'''
score_file = open("score.txt", "a", encoding = "utf8") #어떤 파일을 이어쓰고 싶을 때 "a"
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #바로 write 로 쓰면 줄바꿈이 없기 때문에 \n으로 줄바꿈 해줌
score_file.close()
'''
'''
score_file = open("score.txt", "r", encoding = "utf8") # "r" read 파일에 있는 것을 읽어오는 방법
print(score_file.read()) # 파일에 있는 모든 내용을 터미널에 불러옴
score_file.close()
'''
'''
score_file = open("score.txt", "r", encoding = "utf8") 
print(score_file.readline()) # 줄별로 읽기 동작을 수행 한 후 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline()) # 영어
print(score_file.readline()) # 과학
print(score_file.readline()) # 코딩
score_file.close()
'''

'''
# 총 길이를 모르는 txt 를 읽을떄
score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()
'''


score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line)
score_file.close()