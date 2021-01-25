

# Ex05-Quiz_set.py

sub_python = {"류현진", "이강인", "추신수", "손흥민", "헐크"}
sub_java = {"이강인", "아이언맨", "헐크", "류현진", "토르"}
print("python : ", sub_python)
print("java   : ", sub_java)
print()


'''
python 과 java를 모두 수강중인 학새을 구하는 코드를 작성하세요
'''
print("- python, java 동시 수강 -")
i_sub = sub_python.intersection(sub_java)
print(i_sub)
print()

'''
python 과 java 과목 중에서 python만 듣는 학생을 구하는 코드를 작성하세요
'''
print("- python 수강 -")
d_sub = sub_python.difference(sub_java)
print(d_sub)
print()


'''
입력을 사용해서 java 과목에서 학생을 삭제하는 코드를 작성하세요
'''
r_name = input("java 수강 취소 이름 입력 > ")

if r_name in sub_java:
    sub_java.remove(r_name)
    print("{} 학생 java 수강 취소".format(r_name))
else:
    print("등록된 이름이 아닙니다...")
print("java   : ", sub_java)





























