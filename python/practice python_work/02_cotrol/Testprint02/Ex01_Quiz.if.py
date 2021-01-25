# Q-1 두수 중 큰수를 찾는 코드를 작성하세요
#     - 두수는 다른 수 입니다.(if문으로 구현)

v1 = int(input())
v2 = int(input())
if v1>v2 :
    print("더 큰 수는 {}입니다.".format(v1))
if v1<v2 :
    print("더 큰 수는 {}입니다.".format(v2))



# Q-2 세개의 수 중에서 큰수를 찾는 코드를 작성
#     - 세개의 수는 모두 다른 수

p1 = int(input())
p2 = int(input())
p3 = int(input())
if p1>p2 and p1>p3 :
    print("가장 큰 수는 {}입니다.".format(p1))
if p2>p1 and p2>p3 :
    print("가장 큰 수는 {}입니다.".format(p2))
if p3>p1 and p3>p2:
    print("가장 큰 수는 {}입니다.".format(p3))


# Q-3 5의 배수인지를 확인하는 코드를 작성

multiple = int(input())
if multiple % 5 ==0:
    print("{}은 5의 배수입니다.".format(multiple))
if multiple % 5 != 0:
    print("{}은 5의 배수가 아닙니다.".format(multiple))


# Q-4 두수의 합이 2의 배수이면서 3의 배수도 되는지를 확인하는 코드를 작성





# Q-5 두 위치 사이의 거리를 구하는 코드를 작성
#   - 거리의 결과는 무조건 + 값으로 나와야 함

point1 = int(input())
point2 = int(input())
distance = abs(point1-point2)