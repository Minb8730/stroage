# print("python", "java", sep=" ", end="?") # sep로 , 의 값을 정해준다. / end 는 줄바꿈을 하지 않고 다음 문장과 한 줄로 출력
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "Java", file=sys.stdout) #스탠다드 출력
# print("python", "Java", file=sys.stderr) # 에러 처리

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #정렬 방법


# #은행 대기순번표  Ex)001, 002
# for num in range(1, 21):
#     print("대기번호 : "+ str(num).zfill(3))   #ZeroFill() 값이 없는 곳은 0 으로 채워 달라

answer = input("아무 값이나 입력하세요 : ")
# print(type(answer)) -> str(문자열) 값으로 저장됨
print("입렵하신 값은 " + answer + "입니다.")