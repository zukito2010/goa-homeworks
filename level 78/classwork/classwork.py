# 1)
def vowel_indices(word):
    vowels = 'aeiouyAEIOUY'
    res = []
    for i in range(len(word)):
        if word[i] in vowels:
            res.append(i+1)
        else:
            continue
    return res

# 2)
def bumps(road):
    return 'Car Dead' if list(road).count('n') > 15 else 'Woohoo!'

# 3)
def generate_shape(n):
    return '\n'.join([n*'+' for x in range(n)])

# 4)
def count_red_beads(n):
    return 0 if n<2 else (n-1)*2

# 5)
def words_to_marks(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ssplit = list(s)
    res = 0
    for i in ssplit:
        res += alpha.index(i)+1
    return res

# 6)
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

# 7)
def remove_duplicate_words(s):
    res = []
    spl = s.split(' ')
    for i in spl:
        if not i in res:
            res.append(i)
        else:
            continue
    return ' '.join(res)

# 8)
def sort_gift_code(code):
    return ''.join(sorted(code))

# 9)
def show_sequence(n):
    res = [x for x in range(n+1)]
    if n > 0:
        return f"{'+'.join(map(str, res))} = {sum(res)}"
    elif n == 0:
        return "0=0"
    else:
        return f"{n}<0"
    
# 10)
def sum_cubes(n):
    return sum([x**3 for x in range(1,n+1)])