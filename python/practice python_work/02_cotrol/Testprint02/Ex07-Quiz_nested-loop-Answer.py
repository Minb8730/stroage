

# Ex07-Quiz_nested-loop.py

'''
아래와 같은 형태로 구구단을 출력하는 코드를 작성하세요
2 * 1 = 2,    3 * 1 = 3,   4 * 1 = 4,  ...  9 * 1 = 9
2 * 2 = 4,    3 * 2 = 6,   4 * 2 = 8,  ...  9 * 2 = 18
                  .............
2 * 9 = 18,   3 * 9 = 27,  4 * 9 = 36,  ... 9 * 9 = 81 
'''
# for su in range(1, 10):
#     for dan in range(2, 10):
#         print("{:2} x {:2} = {:2}".format(dan, su, dan*su), end="")
#         if dan != 9:
#             print(", ", end="")
#     print()
# print()



'''
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
'''
# for o in range(1, 6):
#     for n in range(1, 6):
#         print(n, end=" ")
#     print()
# print()


'''
1  2  3  4  5
   2  3  4  5
      3  4  5
         4  5
            5
'''
for o in range(1, 6):
    sp = 1
    for n in range(1, 6):
        if sp < o:  
            print(" ", end=" ")
        else:
            print(n, end=" ")
        sp += 1
    print()
print()


'''
5  4  3  2  1
5  4  3  2  
5  4  3  
5  4  
5  
'''
# for o in range(5):
#     for n in range(5, 0, -1):
#         if n > o:  
#             print(n, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print()


'''
1  2  3  4  5
2  3  4  5  1
3  4  5  1  2
4  5  1  2  3
5  1  2  3  4  
 '''
# for o in range(5):
#     for n in range(1, 6):
#         data = o + n  
#         if data > 5:
#             data %= 5
#         print(data, end=" ")
#     print()
# print()




























