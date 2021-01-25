sub_python = {"류현진", "이강인", "추신수", "손흥민", "헐크"}
sub_java = {"이강인", "아이언맨", "헐크", "류현진", "토르"}

'''
python 과 java를 모두 수강중인 학생을 구하는 코드를 작성
'''
# print(sub_python & sub_java)
# print(sub_python.intersection(sub_java))

'''
python 과 java 과목 중에서 python 만 듣는 학생을 구하는 코드를 작성
'''
# print(sub_python - sub_java)
# print(sub_python.difference(sub_java))

'''
입력을 사용해서 java 과목에서 학생을 삭제하는 코드를 작성
'''

st = input("java 삭제 학생 :")
sub_java.remove(st)
print(sub_java)
    