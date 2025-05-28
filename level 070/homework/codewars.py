# 1) https://www.codewars.com/kata/56f3f6a82010832b02000f38/train/python
def describe_age(a):
    return f"You're a(n) {'kid'if a<13 else'teenager'if a<18 else'adult'if a< 65 else 'elderly'}"

# 2) https://www.codewars.com/kata/57ab2d6072292dbf7c000039/train/python
def correct_polish_letters(st): 
    diacritic_map = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z'
    }
    return ''.join(diacritic_map.get(char, char) for char in st)

# 3) https://www.codewars.com/kata/5786f8404c4709148f0006bf/train/python
def starting_mark(height):
    x1, y1 = 1.52, 9.45
    x2, y2 = 1.83, 10.67
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    starting_position = m * height + b
    return round(starting_position, 2)

# 4) https://www.codewars.com/kata/57096af70dad013aa200007b/train/python
def logical_calc(array, op):
    res = array[0]
    for i in array[1:]:
        if op == 'AND':
            res = res and i
        elif op == 'OR':
            res = res or i
        elif op == 'XOR':
            res = res != i
    return res

# 5) https://www.codewars.com/kata/545993ee52756d98ca0010e1/train/python
def none(lst, func):
    if not lst:
        return True
    for i in lst:
        if func(i):  
            return False
    return True

# 6) https://www.codewars.com/kata/55a75e2d0803fea18f00009d/train/python
def find_slope(points):
    x1, y1, x2, y2 = points
    if x1 == x2:
        return "undefined"
    return str((y2 - y1) // (x2 - x1))

# 7) https://www.codewars.com/kata/55e8aba23d399a59500000ce/train/python
class Hero:
    def __init__(self, name="Hero"):
        self.name = name
        self.position = "00"
        self.health = 100
        self.damage = 5
        self.experience = 0

# 8) https://www.codewars.com/kata/65128732b5aff40032a3d8f0/train/python
def neutralise(s1, s2):
    res = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            res += s1[i]
        else:
            res += '0'
    return res

# 9) https://www.codewars.com/kata/56aed32a154d33a1f3000018/train/python
def my_first_kata(a, b):
    if isinstance(a, int) and isinstance(b, int): 
        if a == 0 or b == 0:
            return False 
        return a % b + b % a
    return False

# 10) https://www.codewars.com/kata/587c2d08bb65b5e8040004fd/train/python
def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    return round((ppg / mpg) * 48, 1)

# 11) https://www.codewars.com/kata/59c287b16bddd291c700009a/train/python
def ice_brick_volume(radius, bottle_length, rim_length):
    return (2 * radius) ** 2 * (bottle_length - rim_length) / 2

# 12) https://www.codewars.com/kata/57bfea4cb19505912900012c/train/python
def symmetric_point(p, q):
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]

# 13) https://www.codewars.com/kata/5713bc89c82eff33c60009f7/train/python
def to_freud(sentence):
    if sentence == '':
        return ''
    times = sentence.split(" ")
    res = []
    for i in range(len(times)):
        res.append('sex')
    
    return ' '.join(res)

# 14) https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python
def two_highest(arg1):
    a = list(set(arg1))
    if len(a) < 2:
        return a
    return [sorted(a)[-1], sorted(a)[-2]]

# 15) https://www.codewars.com/kata/573f5c61e7752709df0005d2/train/python
def merge_arrays(first, second): 
    return sorted(list(set(first+second)))

# 16) https://www.codewars.com/kata/5890d8bc9f0f422cf200006b/train/python
def excluding_vat_price(price):
    if price is None:
        return -1
    return round(price / 1.15, 2)

# 17) https://www.codewars.com/kata/65ba420888906c1f86e1e680/train/python
def collinearity(x1, y1, x2, y2):
    return x1 * y2 == x2 * y1

# 18) https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python
# def alias_gen(first, last):
#     first_char = first[0].upper()
#     last_char = last[0].upper()
#     if first_char in FIRST_NAME and last_char in SURNAME:
#         return f"{FIRST_NAME[first_char]} {SURNAME[last_char]}"
#     return "Your name must start with a letter from A - Z."

# 19) https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/train/python
def html_special_chars(data): 
    data = data.replace('&', '&amp;')
    data = data.replace('<', '&lt;')
    data = data.replace('>', '&gt;')
    data = data.replace('"', '&quot;')
    return data

# 20) https://www.codewars.com/kata/55d8618adfda93c89600012e/train/python
def what_is(x):
    if isinstance(x,int):
        if x is 42:
            return 'everything'
        elif x == 42 * 42:
            return 'everything squared'
        return 'nothing'
    else:
        return 'nothing'
