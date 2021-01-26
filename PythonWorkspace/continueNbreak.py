absent = [2, 5]
no_book = [7]
for student in range (1, 11) :
    if student in absent:
        continue #문장을 실행하지 않고 스킵한 후 다음 문장을 실행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break #이후 문장을 실행하지 않고 탈출
    print("{0}아 책 읽어봐".format(student))
