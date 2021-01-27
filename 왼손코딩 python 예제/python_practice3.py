#21 House Password
'''
Input - A password as a str (10자 이상, 대문자, 소문자, 숫자를 최소 한개씩 포함)
Output - True or False boolean
'''

def house_password(pw):
    if len(pw) < 10:
        return False
    elif pw.islower() == True:
        return False
    elif pw.isupper() == True:
        return False
    
    return any(i.isdigit() for i in pw)



a = house_password('93390053aA')
b = house_password( '1234a')
print(a)
print(b)


#22 Non-unique Elements
'''
Input - A list of int
Output - An iterable of int
리스트 안의 수가 중복 2개 이상일때만 출력하고 순서는 그대로 
'''

def non_unique_elements(num_lst):
    return list(a for a in num_lst if num_lst.count(a) > 1)

a = non_unique_elements([1,1,2,3,3,4,4,4,5,6,7])
print(a)


#23 Monkey typing
'''
Input - Two arg, A text as a str and words as a set of str
Output - The number of words in the text as an int
무작위로 배열되어 있는 문자속에 찾고자 하는 단어가 몇개 있는지 숫자로 출력. 중복으로 세기 불가능 

'''
def monkey_typing(text, words):
    cnt = 0
    for i in words:
        if i in text.lower():
            cnt += 1
    return cnt


a = monkey_typing("How arejsduhiq you?",{"how","are","you"})
print(a)


#24 All the same
'''
Input - List
Output - Bool
리스트 안의 값이 전부 같은지 다른지 bool 로 출력

'''
def all_the_same(lst):
    return len(set(lst)) <= 1 

a = all_the_same([1,1,1])
print(a)
b = all_the_same([1,2,1])
print(b)


#25 Median
'''
Input - An array as a list of int
Output - The median as a float or an int
중간값을 구하자. 리스트의 갯수가 홀수라면 중간값은 가운데 수, 짝수라면 가운데 두수 합의 /2
'''


def median(num_lst):
    num_lst.sort()
    half = len(num_lst) // 2

    return (num_lst[half] + num_lst[-half -1 ]) / 2


a = median([1,2,3,4,5,6])
print(a)