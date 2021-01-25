'''
반복문
- 같은 코드 또는 유사한 코드를 여러번 실행 할 때 사용하는 제어문

for 문
-for 변수 in 목록 :
    실행 코드

> 목록에 값이 있으면 그 값을 in 왼쪽의 변수에 넘겨주면서 반복문의 코드를 실행합니다.


'''

'''
testA = "123"
for v in testA:
    print(v)

kor = "가나다라마"
for t in kor:
    print(t, end= "")
    '''

'''
range()
- range() 함수는 연속적인 수의 리스트를 만드는 함수 입니다.
- range(시작값, 종료값, 증감값)
 > 시작값 : 기본값 0
   증감값 : 기본값 +1
            값을 감소 시킬때에는 감소값을 지정해야 합니다.
 > 실제 생성되는 데이터의 마지막 값은 '종료 -1' 까지 입니다.

'''
'''
range( end )
- 시작의 기본값 0 ~ end-1 까지 생성합니다.
'''
# for v in range(5):
#     print(v, end = "")

'''
range(start, end)
- start ~ end -1 까지 생성합니다.
'''
# for v in range (1,6):
#     print(v, end = "")

'''
range(start, end, step)
-start
'''

# for v in range( 1, 10, 2):
#     print(v, end = "")


'''
1~n 까지의 합
'''
# sum = 0

# for i in range(1, 11):
#     sum += i

# print(sum)


'''
특정 범위 사이의 n의 배수
'''
start = 1  
end = 30
n =3  #배수
count = 0

print("{} ~ {} 사이의 {}의 배수".format(start, end, n))
for v in range(start, end+1):
    if v % n == 0:
        print(v, end = " ")
        count += 1
print()

print("{} 의 배수 개수 : {}".format(n, count))

for v in range(n, end+1, n):
    print(v, end = " ")

