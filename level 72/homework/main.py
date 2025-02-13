# 1) https://www.codewars.com/kata/53cf459503f9bbb774000003/train/python
class Python:
    def __init__(self, name):
        self.name = name 

# 2) https://www.codewars.com/kata/56214b6864fe8813f1000019/train/python
# from preloaded import *

health = 100
position = 0
coins = 0

# def main():
    # roll_dice()
    # move()    
    # combat()  
    # get_coins()
    # buy_health()
    # print_status()

# 3) https://www.codewars.com/kata/521cd52e790405a74800032c/train/python
def wrap(value):
    return {"value": value}

# 4) https://www.codewars.com/kata/5803956ddb07c5c74200144e/train/python
import math

def dating_range(age):
    if age <= 14:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        min_age = age // 2 + 7
        max_age = (age - 7) * 2
        
    return f"{min_age}-{max_age}"

# 5) https://www.codewars.com/kata/56a29b237e9e997ff2000048/train/python
rooms = {
    "room1": {
        "name": "The Dark Chamber",
        "description": "A dark and eerie room with a musty smell. There are strange symbols etched on the walls.",
        "completed": False
    },
    "room2": {
        "name": "The Library",
        "description": "A vast library with towering bookshelves. A sense of mystery lingers in the air.",
        "completed": False
    },
    "room3": {
        "name": "The Hidden Vault",
        "description": "A small, locked vault hidden behind a secret door. The air is thick with tension.",
        "completed": False
    }
}

# 6) https://www.codewars.com/kata/545af3d185166a3dec001190/train/python
def each_cons(lst, n):
    return [lst[i:i + n] for i in range(len(lst) - n + 1)]

# 7) https://www.codewars.com/kata/59126992f9f87fd31600009b/train/python
def whose_move(last_player, win):
    if win:
        return last_player
    elif last_player == 'white':
        return 'black'
    else:
        return 'white'

# 8) https://www.codewars.com/kata/56c22c5ae8b139416c00175d/train/python
def job_matching(candidate, job):
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError("Both candidate and job must have min_salary and max_salary keys.")
    candidate_min_wiggle = candidate['min_salary'] * 0.9
    return candidate_min_wiggle <= job['max_salary']

# 9) https://www.codewars.com/kata/5703c093022cd1aae90012c9/train/python
def find(a,e):
    return a.index(e) if e in a else "Not found"

# 10) https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/train/python
def sorter(textbooks):
    return sorted(textbooks, key=str.lower)

# 11) https://www.codewars.com/kata/586ee462d0982081bf001f07/train/python
def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n

# 12) https://www.codewars.com/kata/574c5075d27783851800169e/train/python
def animals(heads, legs):
    if heads < 0 or legs < 0 or legs % 2 != 0:
        return "No solutions"
    
    cows = (legs - 2 * heads) // 2
    chickens = heads - cows
    
    if chickens < 0 or cows < 0:
        return "No solutions"
    
    return (chickens, cows)

# 13) https://www.codewars.com/kata/5f9f43328a6bff002fa29eb8/train/python
def approx_equals(computed_value, reference_value):
    tolerance = 0.001
    return abs(computed_value - reference_value) <= tolerance

# 14) https://www.codewars.com/kata/56019d3b2c39ccde76000086/train/python
# def do_turn():
#     roll_dice()
#     move()
#     combat()
#     get_coins()
#     buy_health()
#     print_status()

# 15) https://www.codewars.com/kata/575fa9afee048b293e000287/train/python
def how_much_water(water, load, clothes):
    if clothes < load:
        return "Not enough clothes"
    elif clothes > load * 2:
        return "Too much clothes"
    else:
        extra_clothes = clothes - load
        water_needed = water * (1.1 ** extra_clothes)
        return round(water_needed, 2)

# 16) https://www.codewars.com/kata/559f860f8c0d6c7784000119/train/python
def any_arrows(arrows):
    for arrow in arrows:
        if 'damaged' not in arrow or arrow['damaged'] is False:
            return True
    return False

# 17) https://www.codewars.com/kata/566dc566f6ea9a14b500007b/train/python
def kata_13_december(lst):
    return [i for i in lst if i % 2 != 0]

# 18) https://www.codewars.com/kata/566dc05f855b36a031000048/train/python
def add_extra(list_of_numbers):
    new_list = list_of_numbers.copy()
    new_list.append(13)
    return new_list

# 19) https://www.codewars.com/kata/59c8b38423dacc7d95000008/train/python
def is_valid(formula):
    if 1 in formula and 2 in formula:
        return False
    if 3 in formula and 4 in formula:
        return False
    if (5 in formula and 6 not in formula) or (6 in formula and 5 not in formula):
        return False
    if not (7 in formula or 8 in formula):
        return False
    return True

# 20) https://www.codewars.com/kata/54598e89cbae2ac001001135/train/python
def any_(lst, func):
    if not lst:
        return False
    for item in lst:
        if func(item):
            return True 
    
    return False  
