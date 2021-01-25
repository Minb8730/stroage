'''
format method 메서드
 - print('{}'.format(데이터))
  > 문자열 출력안의 {} (포멧필드) 위치에 데이터를 출력

 더욱 직관적이고 편리할 수 있음


dataA = 100
print("data :", dataA)
print("data : {}".format(dataA))


dataB = 200
print("dataB :", dataB)
print()



print("dataA :", dataA, "- dataB :", dataB)
print("dataA : {} - dataB : {}".format(dataA, dataB))

title = "python"
name = "귀도 반 로섬"
print("{} 설계자 : {}".format(title, name))

'''

''' ---------------------------------------------------------------------------------------------
소수점 자리 조정
- { :. 소수점자리f }
 > 지정한 소수점 자리까지 출력

height = 123.1234
print("높이 : {}".format(height))
print("높이 : {:.1f}".format(height))

'''



'''-------------------------------------------------------------------------------------------------
출력 필드 폭 지정
- { :정수 }
 > 해당 위치에 정수값 만큼의 공간확보를 하고 데이터를 출력

 - { :기호 정수}
  > 기호 : 숫자는 기본이 오른쪽 맞춤이고, 문자열은 기본이 왼쪽 맞춤
    < : 왼쪽 맞춤
    ^ : 가운데 맞춤
    > : 오른쪽 맞춤



value = 123
print("{}".format(value))
print("{:5}".format(value))
print("{:<5}#".format(value))
print("{:^5}#".format(value))


word = "abc"
print("{}".format(word))
print("{:5}".format(word))
print("{:<5}#".format(word))
print("{:^5}#".format(word))


#은 그냥 공간 확인 예시용으로 쓴것일 뿐
'''



