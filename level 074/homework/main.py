# 1) https://www.codewars.com/kata/58e3f824a33b52c1dc0001c0/train/python
import math
def circle_area(circle):
    return circle.radius ** 2 * math.pi

# 2) https://www.codewars.com/kata/596e4ef7b61e25981200009f/train/python
import math
from typing import Tuple

def aspect_ratio(x: int ,y: int) -> Tuple[int, int]:
    return (math.ceil(y * 16 / 9), y)

# 3) https://www.codewars.com/kata/5b7ea71db90cc0f17c000a5a/train/python
def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    R = 0.082  
    temp_K = temp + 273.15
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    P_total = (n1 + n2) * R * temp_K / volume
    
    return P_total

# 4) https://www.codewars.com/kata/644b17b56ed5527b09057987/train/python
STRANGE_STRING = 'ß'

# 5) https://www.codewars.com/kata/58e43389acfd3e81d5000a88/train/python
import math
def circle_circumference(circle):
    return  2 * math.pi * circle.radius

# 6) https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd/train/python
def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst

# 7) https://www.codewars.com/kata/570bcd9715944a2c8e000009/train/python
def sc(n: int) -> str:
    """Given n, returns a string which fulfills with the Kata task.
    """
    if n <= 1:
        return ""
    elif n <= 6:
        res = []
        for i in range(n-1):
            res.append("Aa~")

        res.append("Pa!")
        res.append("Aa!")
        return ' '.join(res)
    else:
        res = []
        for i in range(n-1):
            res.append("Aa~")
        return ' '.join(res) + ' Pa!'
    
# 8) https://www.codewars.com/kata/5732d3c9791aafb0e4001236/train/python
def round_it(n):
    str_n = str(n)
    left, right = str_n.split('.')
    
    if len(left) < len(right):
        return int(n) + 1 if n > 0 else int(n)
    elif len(left) > len(right):
        return int(n)
    else:
        return round(n)

# 9) https://www.codewars.com/kata/57037ed25a7263ac35000c80/train/python
import urllib.parse

def generate_link(username):
    encoded_username = urllib.parse.quote(username)
    return f"http://www.codewars.com/users/{encoded_username}"

# 10) https://www.codewars.com/kata/56bc1acf66a2abc891000561/train/python
# from preloaded import greek_alphabet

# def greek_comparator(lhs, rhs):
#     index_lhs = greek_alphabet.index(lhs)
#     index_rhs = greek_alphabet.index(rhs)
#     if index_lhs < index_rhs:
#         return -1
#     elif index_lhs > index_rhs:
#         return 1 
#     else:
#         return 0   
    
# 11) https://www.codewars.com/kata/5b609ebc8f47bd595e000627/train/python
def convert_mass(mass, unit):
    if unit == "kg":
        return mass
    elif unit == "g":
        return mass / 1000
    elif unit == "mg":
        return mass / 1000000
    elif unit == "μg":
        return mass / 1000000000
    elif unit == "lb":
        return mass * 0.453592
    else:
        raise ValueError(f"Unknown mass unit: {unit}")

def convert_distance(distance, unit):
    if unit == "m":
        return distance
    elif unit == "cm":
        return distance / 100
    elif unit == "mm":
        return distance / 1000
    elif unit == "μm":
        return distance / 1000000
    elif unit == "ft":
        return distance * 0.3048
    else:
        raise ValueError(f"Unknown distance unit: {unit}")

def solution(arr_val, arr_unit):
    mass1, mass2, distance = arr_val
    unit_mass1, unit_mass2, unit_distance = arr_unit
    mass1_kg = convert_mass(mass1, unit_mass1)
    mass2_kg = convert_mass(mass2, unit_mass2)
    distance_m = convert_distance(distance, unit_distance)
    G = 6.67 * 10**-11
    force = G * mass1_kg * mass2_kg / (distance_m ** 2)
    
# 12) https://www.codewars.com/kata/57238766214e4b04b8000011/train/python
def change_me(money): 
    changable = ["£5", "£2", "£1", '50p', '20p']
    if not money in changable:
        return money
    elif money == "£5":
        return '20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p'
    elif money == "£1":
        return '20p 20p 20p 20p 20p'
    elif money == "£2":
        return '20p 20p 20p 20p 20p 20p 20p 20p 20p 20p'
    elif money == '50p':
        return '20p 20p 10p'
    elif money == '20p':
        return '10p 10p'

# 13) no 8kyus left