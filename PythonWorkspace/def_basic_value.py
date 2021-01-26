'''
def profile(name, age, main_lang): #역슬러쉬 \ 로 긴 문장을 다룰때 출력에서 변화 없이 줄바꿔서 이용할 수 있음.
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 26, "자바")
'''

#같은 학교, 학년, 반, 수업
#이때 기본값을 사용

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t 나이 : {1}\t 주 사용언어 : {2}".format(name, age, main_lang))
    
profile("유재석")
profile("김태호")
