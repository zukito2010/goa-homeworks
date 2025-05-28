# 1)
def xo(s):
    a = s.lower()
    countx = a.count("x")
    counto = a.count("o")
    return countx == counto

# 2)
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# 3)
def find_short(s):
    lens = [len(word) for word in s.split()]
    return min(lens)

# 4)
def solution(string, ending):
    return string.endswith(ending)

# 5)
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

# 6)
def mygcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# 7)
def my_languages(result):
    passing_languages = [language for language, score in result.items() if score >= 60]
    passing_languages.sort(key=lambda lang: result[lang], reverse=True)
    
    return passing_languages

# 8)
def add(n):
    def adder(x):
        return x + n
    return adder

# 9)
def adjacent_element_product(arr):
    max_product = float('-inf')
    for i in range(len(arr) - 1):
        product = arr[i] * arr[i + 1]
        max_product = max(max_product, product)
    return max_product

# 10)
def to_float_array(arr): 
    return [float(x) for x in arr]
