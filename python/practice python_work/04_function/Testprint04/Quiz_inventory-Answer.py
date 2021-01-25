

# Quiz_inventory.py

'''
제품 정보
- 제품번호, 제품명, 가격, 수량
'''
inventory = list()

# 메뉴 실행 함수
def menu():
    print("- 제 품 관 리 -")
    print("1.등록  2.검색  3.수정  4.삭제  5.목록")
    select = int(input("선택 >> "))
    return select

# 제품 등록
def insert():
    product = dict()
    print("- 제 품 등 록 -")
    product['제품번호'] = input("제품번호 > ")
    product['제품명'] = input("제품명 > ")
    product['가격'] = int(input("가격 > "))
    product['수량'] = int(input("수량 > "))
    inventory.append(product)

# 하나의 제품 정보 출력하는 함수
def proView(pro):
    print("{} - {} - {} - {}".format(pro['제품번호'], pro['제품명'], pro["가격"], pro['수량']))

# 제품 목록
def listView():
    global inventory
    print("\t- 제 품 목 록 -")
    for pro in inventory:
        proView(pro)

# 제품 검색 함수
def search():
    print("- 제 품 검 색 - ")
    scode = input("제품번호 입력 > ")
    for pro in inventory:
        if scode == pro['제품번호']:
            proView(pro)
            break
    else:
        print("검색 실패!!")
    
# 제품 수정하는 함수
def alter():
    print("- 제 품 수 정 -")
    acode = input("제품번호 입력 > ")
    for idx in range(len(inventory)):
        if acode == inventory[idx]['제품번호']:
            inventory[idx]['가격'] = int(input("가격 > "))
            inventory[idx]['수량'] = int(input("수량 > "))
            break
    else:
        print("수정 실패!!")

# 제품 삭제하는 함수
def remove():
    print("- 제 품 삭 제 -")
    rcode = input("제품번호 입력 > ")
    for pro in inventory:
        if rcode == pro['제품번호']:
            inventory.pop(inventory.index(pro))
            break
    else:
        print("삭제 실패!!")

"""--------------------------------------------------"""

proRun = True
while proRun:
    select = menu();

    if select == 1: # 등록
        insert()
    elif select == 2: # 검색
        search()
    elif select == 3: # 수정
        alter()
    elif select == 4: # 삭제
        remove()
    elif select == 5: # 목록
        listView()
    elif select == 0: # 종료
        proRun = False
    else:
        print("선택 오류~")
    print()

else:
    print("- Program end -")






































