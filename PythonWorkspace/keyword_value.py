def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age =20)
profile(main_lang = "자바", age = 25, name = "김태호")
#순서가 뒤섞여도 자리는 함수에 따라감

#가변 인자 -> 인자의 변동 가능성이 있을 때.
'''
#인자가 고정되어 있는 경우, 만약 유재석의 lang 이 하나 더 추가되면 def 에서 lang6 를 추가해야 함.
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age, end =" "))
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "") #함수에 맞춰서 빈칸을 설정
'''
def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age, end =" "))
    for lang in language:
        print(lang, end = "\t")
    print() #줄바꿈을 위해서

profile("유재석", 20, "python", "java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")
