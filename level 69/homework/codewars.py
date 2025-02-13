# 1) https://www.codewars.com/kata/572b6b2772a38bc1e700007a/train/python
def uni_total(s):
    return sum(ord(char) for char in s)

# 2) https://www.codewars.com/kata/5862f663b4e9d6f12b00003b/train/python
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    remaining_blue = blue_start - blue_pulled
    remaining_red = red_start - red_pulled
    
    total_remaining = remaining_blue + remaining_red
    
    return remaining_blue / total_remaining

# 3) https://www.codewars.com/kata/54fdaa4a50f167b5c000005f/train/python
def get_status(is_busy):
    return {"status": "busy" if is_busy else "available"}

# 4) https://www.codewars.com/kata/5b4e779c578c6a898e0005c5/train/python
def draw_stairs(n):
    return "\n".join(" " * i + "I" for i in range(n))

# 5) https://www.codewars.com/kata/55a14f75ceda999ced000048/train/python
def temple_strings(obj, feature): 
    return f'{obj} are {feature}'

# 6) https://www.codewars.com/kata/5d59576768ba810001f1f8d6/train/python
def quadratic(x1, x2):
    a = 1
    b = -(x1 + x2)
    c = x1 * x2
    return (a, b, c)

# 7) https://www.codewars.com/kata/55dc4520094bbaf50e0000cb/train/python
def am_i_wilson(n):
    return n in {5, 13, 563}

# 8) https://www.codewars.com/kata/5763bb0af716cad8fb000580/train/python
def count_squares(cuts):
    return (cuts+1)**3 - (cuts-1)**3

# 9) https://www.codewars.com/kata/57a386117cb1f31890000039/train/python
def parse_float(string):
    try:
        return float(string)
    except :
        return None

# 10) https://www.codewars.com/kata/578a8a01e9fd1549e50001f1/train/python
from datetime import date

def period_is_late(last, today, cycleLength):
    return (today - last).days > cycleLength

# 11) https://www.codewars.com/kata/54dba07f03e88a4cec000caf/train/python
class Dog:
    def __init__(self, breed):
        self.breed = breed
def bark(self):
    return "Woof"

Dog.bark = bark 
snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")

# 13) https://www.codewars.com/kata/572b77262bedd351e9000076/train/python
def first(seq, n=1): 
    return seq[0:n]

# 14) https://www.codewars.com/kata/57280481e8118511f7000ffa/train/python
def split_and_merge(string_, separator):
    words = string_.split(' ')
    modified_words = [separator.join(word) for word in words]
    return ' '.join(modified_words)

# 15) https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python
def cookie(x):
    if isinstance(x, str):
        name = "Zach"
    elif isinstance(x, (float, int)) and not isinstance(x, bool):
        name = "Monica"
    else:
        name = "the dog"

    return f"Who ate the last cookie? It was {name}!"

# 16) https://www.codewars.com/kata/59c1302ecb7fb48757000013/train/python
def type_validation(variable, _type): 
    return _type in str(type(variable))

# 17) https://www.codewars.com/kata/54592a5052756d5c5d0009c3/train/python
def head(x):
    return x[0]

def tail(x):
    return x[1::]

def init(x):
    return x[:-1]

def last(x):
    return x[-1]

# 18) https://www.codewars.com/kata/5eb27d81077a7400171c6820/train/python
import math

def graceful_tipping(bill):
    total = bill * 1.15  
    if total < 10:
        round_to = 1
    else:
        magnitude = 10 ** int(math.log10(total))
        round_to = magnitude // 2 if magnitude >= 20 else 5
    return math.ceil(total / round_to) * round_to

# 19) https://www.codewars.com/kata/55849d76acd73f6cc4000087/train/python
def playerRankUp(pts):
     return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if pts >= 100 else False
 
# 20) https://www.codewars.com/kata/5866fc43395d9138a7000006/train/python
def ensure_question(s):
    return s if s.endswith('?') else s + '?' 