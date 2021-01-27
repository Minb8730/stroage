#01 Say Hi
def say_hi(name, age):
    return "Hi. My name is {} and I'm {} years old".format(name, age)

Alex = say_hi("Alex", 32) 
print(Alex)


#02 Correct sentence
def correct_sentence(sen):
    
    sen = sen[0].upper() + sen[1:]

    if not sen.endswith("."):
        sen += "."
    
    return sen


a = correct_sentence("greetings friends")
print(a)
print()



#03 First world

def first_world(text):
    text = text.replace('.',' ').replace(',', ' ').strip()
    text = text.split()

    return text[0]

txt1 = first_world("Hello world")
print(txt1)
()


#04 Second index

def second_index(text, alphabet):   # text에 들어가는 alphabet 의 2번째로 오는 alphabet의 index를 찾아라 
    if text.count(alphabet) < 2 :
        return None

    first = text.find(alphabet)

    return text.find(alphabet, first + 1)

find_idx = second_index("sims", "s")
print(find_idx)
print()


#05 Between Makers

def between_makers(txt, start, end):
    if start in txt:
        start_idx = txt.find(start) + len(start)
    else:
        start_idx = 0

    if end in txt:
        end_idx = txt.find(end)
    else:
        end_idx = len(txt)
    return txt[start_idx : end_idx]

be = between_makers("What is >apple<", ">", "<")
print(be)

print()

#06 Best Stock

def best_stock(stock_codes):
    max_price = 0
    answer = ''

    for i in stock_codes: # keys 만 가져와서 i 에 입력
        if stock_codes[i] > max_price : # value 값을 출력
            answer = i  # stock 의 이름만 저장

    return i    #stock 의 이름을 반환


stock_market = best_stock({"CAC" : 10.0, "ATX" : 390.2, "WIG" : 1.2})
print(stock_market)

print()


#07 Popular words


# def popular_words(text, arrays):
#     text = text.lower()
#     res = list(text.count(i) for i in arrays)
#     return dict(zip(arrays, res))


def popular_words(text, words):
    text = text.lower()
    splitted_words = text.split()
    answer = {}
    for word in words:
        answer[word] = splitted_words.count(word)
 
    return answer


cnt_word = popular_words(''' When I was One 
I had just begun
When I was Two 
I was nearly new
''',['i','was','three','near' ])


print(cnt_word)
print()





#8 Bigger price

# def bigger_price(find_num, pro_list):
#     mvp_list = []
#     for product in pro_list:
#         mvp_list.append(product[1])

#     mvp_list.sort()
#     return mvp_list[-1:-find_num]          # 실패...

def bigger_price(limit, data):
    return sorted(data, key = lambda x:x['price'], reverse = True)[:limit]
    
pro_list = bigger_price(2, [
{"name":"bread","price":"100"},
{"name":"wine","price":"138"},
{"name":"meat","price":"15"},
{"name":"water","price":"1"}
])

print(pro_list)




#09 Fizz buzz
def fizz_buzz(num):
    if num % 3 ==0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 3 != 0 and num % 5 == 0:
        print("Buzz")
    else:
        print(str(num))


fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(7)
fizz_buzz(21)
fizz_buzz(8)

print()


#10 The Most Numbers
def the_most_numbers(*nums):
    if nums:
        res = max(nums) - min(nums)
        return res
    else:
        return 0

a = the_most_numbers(1,2,3)
b = the_most_numbers(5, -5)
c = the_most_numbers(10.2,-2.2,0,1.1,0.5 )
d = the_most_numbers()

print(a)
print(b)
print(c)
print(d)
print()













