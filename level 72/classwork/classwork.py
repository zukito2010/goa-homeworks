# 1)
import math
def cooking_time(eggs):
    return math.ceil(eggs / 8) * 5

# 2)
def min_sum(arr):
    arr.sort()
    res = 0
    for i in range(len(arr) // 2):
        res += arr[i] * arr[len(arr) - 1 - i]
    
    return res

# 3)
def sum_triangular_numbers(n):
    res = 0
    for i in range(1, n + 1):
        res += i * (i + 1) // 2 
    return res

# 4) 
def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        left = " ".join(arr[:i])
        right = " ".join(arr[i:])
        result.append((left, right))
    return result

# 5)
def switcheroo(s):
    res = ''
    for i in s:
        if i == 'a':
            res += 'b'
        elif i == 'b':
            res += 'a'
        else:
            res += i
    return res

# 6)
def explode(s):
    res = ''
    for i in s:
        for x in range(int(i)):
            res += i
    return res

# 7)
def sort_my_string(s):
    odds = ''
    evens = ''
    for i in range(0,len(s),2):
        evens += s[i]
    for i in range(1,len(s),2):
        odds += s[i]
    return evens +' '+ odds

# 8) 
def filter_string(st):
    nums = '1234567890'
    res = ''
    for i in st:
        if i in nums:
            res += i
        else:
            continue
    return int(res)

# 9)
def largest_pair_sum(numbers): 
    return sorted(numbers)[-1] + sorted(numbers)[-2]

# 10)
def alphabet_war(fight):
    left_side = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
    }
    
    right_side = {
        'm': 4,
        'q': 3,
        'd': 2,
        'z': 1,
    }
    right = 0
    left = 0
    for i in fight:
        if i in 'wpbs':
            left += left_side[i]
        elif i in 'mqdz':
            right += right_side[i]
        else:
            continue
    
    if right > left:
        return "Right side wins!"
    elif left> right:
        return "Left side wins!"
    else:
        return "Let's fight again!"