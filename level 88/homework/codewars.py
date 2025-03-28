# 1) https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python
def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        left = " ".join(arr[:i])
        right = " ".join(arr[i:])
        result.append((left, right))
    return result

# 2) https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/python
def sum_triangular_numbers(n):
    res = 0
    for i in range(1, n + 1):
        res += i * (i + 1) // 2 
    return res

# 3) https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/python
def min_sum(arr):
    arr.sort()
    res = 0
    for i in range(len(arr) // 2):
        res += arr[i] * arr[len(arr) - 1 - i]
    
    return res

# 4) https://www.codewars.com/kata/52b5247074ea613a09000164/train/python
import math
def cooking_time(eggs):
    return math.ceil(eggs / 8) * 5

# 5) https://www.codewars.com/kata/5783d8f3202c0e486c001d23/train/python
def to_float_array(arr): 
    return [float(x) for x in arr]

# 6) https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python
def adjacent_element_product(arr):
    max_product = float('-inf')
    for i in range(len(arr) - 1):
        product = arr[i] * arr[i + 1]
        max_product = max(max_product, product)
    return max_product

# 7) https://www.codewars.com/kata/538835ae443aae6e03000547/train/python
def add(n):
    def addin(x):
        return x + n
    return addin

# 8) https://www.codewars.com/kata/5b16490986b6d336c900007d/train/python
def my_languages(result):
    passing_languages = [language for language, score in result.items() if score >= 60]
    passing_languages.sort(key=lambda lang: result[lang], reverse=True)
    
    return passing_languages

# 9) https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd/train/python
def mygcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# 10) https://www.codewars.com/kata/56484848ba95170a8000004d/train/python
import math

def gps(s, x):
    if len(x) <= 1:
        return 0

    max_speed = 0
    for i in range(1, len(x)):
        delta_distance = x[i] - x[i - 1]
        speed = (3600 * delta_distance) / s
        max_speed = max(max_speed, speed)

    return math.floor(max_speed)

# 1)
# code explaination:
# def solution(s):
# there we take string (s) and for loop it. then we create string named result and check if any of s's letters are upper if they are not they just get added to the result but if they are upper they get added to the result with ' ' before letter.
# def find_missing_letters(s):
# first we define a function find_missing_letter(chars) and give it a list of letters called chars. Then we create a string called letters which is just all the lowercase and uppercase letters in order. After that, we loop through each index i in the chars list, stopping one before the end. Inside the loop, we check if the current letter  and the next one -are directly next to each other in the alphabet. We do this by checking if the position of the current letter in letters plus one is the same as the position of the next letter. If it’s not, that means there’s a letter missing in between. So we return the letter that should be in between .
# group_by_commas(n):
# first we check if number is 3 digits or smaller (which case we wont going to need commas) and return it if it is. then we use for loop on reversed string of that number and add the comma every 3 numbers then we make variable result and reverse list. than we check if result starts with comma if it does we return it starting from second item ([1:]) else just returning it.
# balance (left,right)
# here both left and right are strings made out of exclamation marks and question marks. inside function we have object 'weights' in which !==2 and ?==3. then we create two variables count1 and count2 in which we take our values of left and right respectively (using for loop to determine values). then if count1 and count2 are equal to each other we return balance else if count1>count2 we return 'Left' else we return right (it says or hakuna matata but it will only return right).
# def dir_reduc(arr):
# first we create object opp which makes directions opposite directions. then there is for loop in range of length of that array and inside that for loop it checks if current and next item of an arr are opposites if they are it deletes both else it continues to the next  until there are no more opposites.
# def generate_hashtags(s):
# first we make every word of s capitalized and add it to the # using s = '#' s.title() than we split it and join it to remove spaces and then if it is in range of 2 and 141 we return that hashtag else we return False.
# def rot13(message):
# first we create two variables for alphabet and capitalized alphabet and write both two times in a string (for cases like letters that are in the last). then we create variable result(and make it an empty string). than we check (using for i in range(len(message))) if the number is upper case and also letter if it is we add 13th letter after it to the result variable else if it is empty string(space) we just add it to the result string else if it is a lower case but a letter we still add 13th number after that in alphabet else we will just add result message[i]. and then we return result.
