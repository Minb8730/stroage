
#11 Even the Last
def even_the_last(nums):
    if not nums:
        return 0
    return sum(nums[::2]*nums[-1])

a = even_the_last([0,1,2,3,4,5])
print(a)

b = even_the_last([1,3,5])
print(b)

c = even_the_last([6])
print(c)

d = even_the_last([])
print(d)
print()


#12 Secret message

'''
Input = A text as a string (unicode)
Ouput = The secret message as a string or an empty string
ex) find_message("How are you? Eh, ok. Low or Lower? Ohhh.") = HELLO
'''

# def secret_message(text):
#     upper_list = []
#     for i in text:
#         if i.isupper():
#             (upper_list.append(i))

#     print(upper_list)

def secret_message(text):
    return ''.join(filter(str.isupper, text))


a = secret_message("How are you? Eh, ok. Low or Lower? Ohhh.")
print(a)



#13 Three words 
'''
Input = A string with words
Output = The answer as a boolean

3개의 문자열이 연속으로 나오면 True
'''

def three_words(text):
    cnt = 0
    
    for word in text.split():
        if word.isalpha():
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3 :
            return True

    return False


#14 Index power 

'''
Input = Two arguments. An array as a list of integers and a number as a integer
Output = The result as an integer
index n번째 값의 숫자 x 의 n 제곱을 출력
n이 list 값의 범위를 벗어나면 -1 출력
ex) index_power([1,2,3,4],2) == 9
'''

# def index_power(array, idx):
#     if idx > len(array):
#         return -1
#     return pow(array[idx], idx)

def index_power(array, idx):
    if idx < len(array):
        return array[idx]**idx
    else:
        return -1


index_power([1,2,3,4],2)



#15 Right to Left
'''
Input = A sequence of strings as a tuple of strings
Output = The text as a string
ex) left_join(("left","right", "left", "stop")) == "left,left,left,stop"
'''

def right_to_left(*text):
    return (",".join(text)).replace("right","left")

a = right_to_left("left","right", "left", "stop")
print(a)


#16 Digits Multiplication
'''
Input = A positive integer
Output = The product of the digits as an integer
ex) checkio(123405) = 120
모든 숫자를 각각 곱하고 0은 무시
'''

def digits_multiplication(num):
    res = 1
    for i in str(num):
        if int(i):
            res *= int(i)
    
    return res

a = digits_multiplication(12345)
print(a)



#17 Number base

def number_base(text, num):
    try:
        return int(text, num)
    except ValueError:
        return -1


#18 Absolute Sorting
'''
intup - An array of numbers, a tuple...
output - The list or tuple (but not a generator) sorted by absolute values in ascending order

'''

def absolute_sorting(array):
       return sorted(array, key = abs)


a = absolute_sorting((-20, -5, 10, 15))
print(a)



#19 The Most Frequent
'''
input - a list of string
ouput - a string
가장 자주 사용된 str 
'''
def the_most_frequence(str_lst):
    return max(str_lst, key = str_lst.count)

f = the_most_frequence(['a','b','bi','bi'])
print(f)



#20 Easy Unpack
'''
input - A tuple, at least 3 elements long
output - A tuple
1idx, 2idx, -2idx
'''

def easy_unpack(tu_lst):
    return tu_lst[0], tu_lst[2], tu_lst[-2]

a = easy_unpack((1,2,3,4,5,6,7,9))
print(a)
