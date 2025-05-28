# 1) https://www.codewars.com/kata/57a77726bb9944d000000b06/train/python
def mango(quantity, price_per_mango):
    paid_mangoes = quantity - (quantity // 3)
    return paid_mangoes * price_per_mango

# 2) https://www.codewars.com/kata/524f5125ad9c12894e00003f/train/python
def remainder(a, b):
    larger = max(a, b)
    smaller = min(a, b)
    if larger == 0 and smaller == -1:
        return 0
    if smaller == 0:
        return None
    return larger % smaller

# 3) https://www.codewars.com/kata/5a805d8cafa10f8b930005ba/train/python
def nearest_sq(n):
    return round(n ** 0.5)**2

# 4) https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python
def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    return sum(x for x in range(n, m, n))

# 5) https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/train/python
def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False
    chars = '!@#$%^&*()-=+[]{}\\|;:,<.>/?~'
    for char in chars:
        if char in username:
            return False
    for i in list(username):
        if i.isupper():
            return False
    if len(username.split(' '))> 1:
        return False
    return True

# 6) https://www.codewars.com/kata/568dc014440f03b13900001d/train/python
def get_drink_by_profession(profession):
    profession = profession.lower()
    if profession == "jabroni":
        return "Patron Tequila"
    elif profession == "school counselor":
        return "Anything with Alcohol"
    elif profession == "programmer":
        return "Hipster Craft Beer"
    elif profession == "bike gang member":
        return "Moonshine"
    elif profession == "politician":
        return "Your tax dollars"
    elif profession == "rapper":
        return "Cristal"
    else:
        return "Beer"
    
# 7) https://www.codewars.com/kata/5641a03210e973055a00000d/train/python
def two_decimal_places(n):
    return round(n,2)

# 8) https://www.codewars.com/kata/514a7ac1a33775cbb500001e/train/python
def mystery():
    results = {
    'sanity': 'Hello'}
    return results

# 9) https://www.codewars.com/kata/57158fb92ad763bb180004e7/train/python
def rain_amount(mm):
    if mm <40:
         return f"You need to give your plant {abs(mm -40) }mm of water"
    else:
         return "Your plant has had more than enough water for today!"

# 10) https://www.codewars.com/kata/52adc142b2651f25a8000643/train/python
class Sleigh(object):
    def authenticate(self, name, password):
        if name == "Santa Claus" and password == "Ho Ho Ho!":
            return True
        return False

# 11) https://www.codewars.com/kata/54fe05c4762e2e3047000add/train/python
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew    

    def is_worth_it(self):
        remaining_draft = self.draft - self.crew * 1.5
        if remaining_draft > 20:
            return True
        else:
            return False

# 12) https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/train/python
def to_csv_text(array):
    return '\n'.join([','.join(map(str, row)) for row in array])

# 13) https://www.codewars.com/kata/5720a1cb65a504fdff0003e2/train/python
def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))

# 14) https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/python
import math

def square_area(A):
    r = (2 * A) / math.pi
    area = r ** 2
    return round(area, 2)

# 15) https://www.codewars.com/kata/57faece99610ced690000165/train/python
def remove(st):
    return st.rstrip('!')

# 16) https://www.codewars.com/kata/57faf12b21c84b5ba30001b0/train/python
def remove(st):
    lst = list(st)
    res = []
    for i in lst:
        if not i == '!':
            res.append(i)
    return ''.join(res)+'!'

# 17) https://www.codewars.com/kata/5a0be7ea8ba914fc9c00006b/train/python
def sakura_fall(v):
    if v <= 0:
        return 0
    
    distance = 5*80
    
    return distance/v

# 18) https://www.codewars.com/kata/567bf4f7ee34510f69000032/train/python
def is_digit(n):
    if n.isdigit() and 0<= int(n)<=9:
        return True
    return False

# 19) https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python
def is_digit(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# 20) https://www.codewars.com/kata/57faf7275c991027af000679/train/python
def remove(st, n):
    lst = list(st)
    i = 0
    x = 0
    while i < n and x < len(lst):
        if lst[x] == '!':
            lst.pop(x)
            i += 1
        else:
            x += 1
    return ''.join(lst)
