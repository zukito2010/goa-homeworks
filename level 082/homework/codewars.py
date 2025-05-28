# 1) https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python
import math

def max_multiple(divisor, bound):
    return math.floor(bound/divisor) * divisor

# 2) https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python
def in_asc_order(arr):
    return True if arr == sorted(arr) else False

# 3) https://www.codewars.com/kata/58fa273ca6d84c158e000052/train/python
def digits(n):
    return len(str(n))

# 4) https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python
def flatten_and_sort(array):
    return sorted([x for i in array for x in i])

# 5) https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
def factorial(n):
    res = 1
    for i in reversed(range(1,n+1)):
        res *= i
    return res
    
# 6) https://www.codewars.com/kata/51675d17e0c1bed195000001/train/python
def solution(digits):
    return max(int(digits[i:i+5]) for i in range(len(digits)-4))

# 7) https://www.codewars.com/kata/525e5a1cb735154b320002c8/train/python
def triangular(n):
    return n*(n+1)//2 if n >0 else 0

# 8) https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python
def min_value(digits):
    res = []
    setd = sorted(set(digits))
    for i in setd:
        res.append(str(i))
    return int(''.join(res))

# 9) https://www.codewars.com/kata/514a6336889283a3d2000001/train/python
def get_even_numbers(arr):
    return [x for x in arr if x%2==0]

# 10) https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/python
def evaporator(content, evap_per_day, threshold) -> int:
    days = 0
    limit = content * (threshold / 100)
    
    while content > limit:
        content -= content * (evap_per_day / 100)
        days += 1
    
    return days