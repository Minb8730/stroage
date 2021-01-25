#151
#  리스트에는 네 개의 정수가 저장돼 있다.

# 리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.

# -20
# -3

리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0:
        print(i)



#152
# for문을 사용해서 3의 배수만을 출력하라.

# 리스트 = [3, 100, 23, 44]
#3

리스트 = [3, 100, 23, 44]
for m in 리스트:
    if m % 3 == 0:
        print(m)


#153
# 리스트에서 20 보다 작은 3의 배수를 출력하라

# 리스트 = [13, 21, 12, 14, 30, 18]
# 12
# 18

리스트 = [13, 21, 12, 14, 30, 18]
for n in 리스트:
    if n <20 and n % 3 == 0:
        print(n)


#154
# 리스트에서 세 글자 이상의 문자를 화면에 출력하라

# 리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language

리스트 = ["I", "study", "python", "language", "!"]
for s in 리스트:
    if len(s) >= 3:
        print(s)


#155
# 리스트에서 대문자만 화면에 출력하라.

# 리스트 = ["A", "b", "c", "D"]
# A
# D

리스트 = ["A", "b", "c", "D"]
for u in 리스트:
    if u.isupper() == True:
        print(u)


#156

# 리스트에서 소문자만 화면에 출력하라.

# 리스트 = ["A", "b", "c", "D"]
# b
# c
리스트 = ["A", "b", "c", "D"]
for l in 리스트:
    if l.islower() == True:
        print(l)



#157
# 이름의 첫 글자를 대문자로 변경해서 출력하라.

# 리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
리스트 = ['dog', 'cat', 'parrot']
for c in 리스트:
    print(c.capitalize())



#158
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for r in 리스트:
    r1 = r.split(".")
    print(r1[0])



#159
# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h
print()
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for y in 리스트:
    y1 = y.split(".")
    if y1[1] == "h":
        print(y)




#160
# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h
print()
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for s in 리스트:
    s1 = s.split(".")
    if s1[1] == "h" or s1[1] == "c":
        print(s)









