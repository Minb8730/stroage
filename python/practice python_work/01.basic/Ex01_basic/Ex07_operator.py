'''
산술 연산자
'''
va, vb = 5, 2
print("{} + {} = {}".format(va, vb, va+vb)) #덧셈
print("{} - {} = {}".format(va, vb, va-vb)) #뺼셈
print("{} * {} = {}".format(va, vb, va*vb)) #곱셈
print("{} / {} = {}".format(va, vb, va/vb)) #나눗셈
print("{} % {} = {}".format(va, vb, va%vb)) #나머지
print("{} // {} = {}".format(va, vb, va//vb)) #몫
print("{} ** {} = {}".format(va, vb, va**vb)) #거듭제곱


'''
복합 대입 연산자
- 산술연산자와 대입연산자를 결합해서 사용하는게 가능합니다.
 Ex) a += b -> a = a+b
 a와 b를 더해서 나온 결과를 a 에 대입합니다.
-계산해서 나온 결과를 왼쪽에 대입하기 떄문에, 왼쪽에는 항상 변수가 있어야 함.
'''

vc = 5
print("va :", vc)

vc += 1
print("vc :", vc)

vc -= 2
print("vc :", vc)

# 5 += vc Error

'''
비교 연산자
- 두개의 데이터를 비교 할 때 사용합니다.
 : <, >, <=, >=
  == 서로 같으면 참
  != 서로 다르면 참
- 비교해서 나온 결과를 True(참), False(거짓) 으로 표시합니다.
'''

ve, vf = 7, 9
print("ve : {} - vf : {}".format(ve, vf))
print("ve > 10 :", ve > 10)
print("ve <= 10 :", ve <= 10)
print("ve == vf :", ve == vf)
print("ve != vf :", ve != vf)



'''
논리 연산자
- and : 두개의 조건식이 모두 참일떄 참
    > 조건식_a and 조건식_b

- or : 두개의 조건식 중에서 하나만 참이면 참
    > 조건식_a or 조건식_b

- not : 참은 거짓으로, 거짓은 참으로 변경

'''

vg, vh = 10, 15
print("vg : {} - : {}".format(vg, vh))
print("vg > 10 and vh < 20 :",vg > 10 and vh < 20 )
print("vg <= 10 and vh < 20 :", vg <= 10 and vh < 20)

print("vg == 10 or vh > 20 :", vg == 10 or vh > 20)
print("vg > 10 or vh > 20 :", vg > 10 or vh > 20)

print("not False :", not False)
print("not vg :", not vg)


'''
식별 연산자
- 자료형을 확인하는 연산자
- type() is 자료형
    > type 안의 자료형이 is 뒤에 자료형과 같으면 참

type() is not 자료형
    > type 안의 자료형이 is not 뒤에 자료형과 다르면 참
'''

vi = 7
print("vi :", vi)
print("type(vi) is int :", type(vi) is int )
print("type(vi) is not int", type(vi) is not int)
print("type(vi) is float", type(vi) is float)


'''
멤버 연산자
 - n in ()
    > n 의 값이 오른쪽의 () 안에 있으면 참

 - n not in ()
    > n 의 값이 오른쪽의 () 안에 없으면 참 

'''

vj = 5
print("vj :", vj)
print("vj in (2, 6, 4)", vj in (2, 6, 4))
print("vj in (2, 8, 3)", vj in (2, 8, 3))
print("vj not in (2, 8, 3)", vj not in (2, 8, 3))


'''
비트 연산자
-&  :비트단위 and 연산
-|  :비트단위 or 연산
-^  :비트단위 xor 연산 ( 비트값이 같으면 0, 다르면 1)
-~  :비트 부정 (비트 값이 0 -> 1, 1 -> 0 으로 변환)
-<< >>  :쉬프트 연산자 (비트값 전체를 왼쪽 or, 오른쪽으로 이동) # 왼쪽으로 한번씩 이동할 때마다 값이 배가 되고 오른쪽으로는 반값이 됨
bin - 해당 10진수를 2진수로 바꾸어주는 명령어
'''

vk, vl = 10, 9
print("vk : {:3} , {:10}".format(vk, bin(vk)))
print("vl : {:3} , {:10}".format(vl, bin(vl)))
print()
print("vk & vl : {:3} , {:10}".format(vk & vl, bin(vk & vl)))
print("vk | vl : {:3} , {:10}".format(vk | vl, bin(vk | vl)))
print("vk ^ vl : {:3} , {:10}".format(vk ^ vl, bin(vk ^ vl)))
print(" ~vk : {:3} , {:10}".format(~vk, bin(~vk)))
print("vk <<2 : {:3} , {:10}".format(vk <<2, bin(vk <<2))) 
