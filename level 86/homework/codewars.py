# 1) https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/python
import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    return math.floor(sum([age_1**2,age_2**2,age_3**2,age_4**2,age_5**2,age_6**2,age_7**2,age_8**2])**0.5)//2

# 2) https://www.codewars.com/kata/580a4734d6df748060000045/train/python
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr,reverse=True):
        return 'yes, descending'
    else:
        return 'no'
    
# 3) https://www.codewars.com/kata/59a8570b570190d313000037/train/python
def sum_cubes(n):
    return sum([x**3 for x in range(1,n+1)])

# 4) https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python
def show_sequence(n):
    res = [x for x in range(n+1)]
    if n > 0:
        return f"{'+'.join(map(str, res))} = {sum(res)}"
    elif n == 0:
        return "0=0"
    else:
        return f"{n}<0"

# 5) https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3/train/python
def sort_gift_code(code):
    return ''.join(sorted(code))

# 6) https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python
def remove_duplicate_words(s):
    res = []
    spl = s.split(' ')
    for i in spl:
        if not i in res:
            res.append(i)
        else:
            continue
    return ' '.join(res)

# 7) https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python
def even_numbers(arr,n):
    res = []
    for i in arr[::-1]:
        if i % 2 == 0:
            if len(res) == n:
                continue
            else:
                res.append(i)
        else:
            continue
    return res[::-1]

# 8) https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python
def words_to_marks(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ssplit = list(s)
    res = 0
    for i in ssplit:
        res += alpha.index(i)+1
    return res

# 9) https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/python
def count_red_beads(n):
    return 0 if n<2 else (n-1)*2

# 10) https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python
def generate_shape(n):
    return '\n'.join([n*'+' for x in range(n)])

# 11) https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python
def bumps(road):
    return 'Car Dead' if list(road).count('n') > 15 else 'Woohoo!'
