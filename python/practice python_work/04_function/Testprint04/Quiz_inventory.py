

# Quiz_inventory.py

'''
제품 정보
- 제품번호, 제품명, 가격, 수량
'''
inventory = list()

def menu():
    print("- 제 품 관 리 -")
    print("1.등록  2.검색  3.수정  4.삭제  5.목록")
    select = int(input("선택 >> "))
    return select

"""--------------------------------------------------"""

proRun = True
while proRun:
    select = menu();

    if select == 1: # 등록
        pass
    elif select == 2: # 검색
        pass
    elif select == 3: # 수정
        pass
    elif select == 4: # 삭제
        pass
    elif select == 5: # 목록
        pass
    elif select == 0: # 종료
        proRun = False
    else:
        print("선택 오류~")
    print()

else:
    print("- Program end -")






































