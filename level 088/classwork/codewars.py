# 1) https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
def vowel_indices(word):
    vowels = 'aeiouyAEIOUY'
    res = []
    for i in range(len(word)):
        if word[i] in vowels:
            res.append(i+1)
        else:
            continue
    return res

# 2) https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python
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

# 3) https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python
def largest_pair_sum(numbers): 
    return sorted(numbers)[-1] + sorted(numbers)[-2]

# 4) https://www.codewars.com/kata/55b051fac50a3292a9000025/train/python
def filter_string(st):
    nums = '1234567890'
    res = ''
    for i in st:
        if i in nums:
            res += i
        else:
            continue
    return int(res)

# 5) https://www.codewars.com/kata/580755730b5a77650500010c/train/python
def sort_my_string(s):
    odds = ''
    evens = ''
    for i in range(0,len(s),2):
        evens += s[i]
    for i in range(1,len(s),2):
        odds += s[i]
    return evens +' '+ odds

# 6) https://www.codewars.com/kata/585b1fafe08bae9988000314/train/python
def explode(s):
    res = ''
    for i in s:
        for x in range(int(i)):
            res += i
    return res

# 7) https://www.codewars.com/kata/57f759bb664021a30300007d/train/python
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

# 8) 