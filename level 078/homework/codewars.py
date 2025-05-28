# 1) https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
def printer_error(s):
    alphas = 'nopqrstuvwxyz'
    res = 0
    for i in s:
        if i in alphas:
            res+=1
    return f'{res}/{len(s)}'

# 2) https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
def binary_array_to_number(arr):
    st = ''.join([str(x) for x in arr])
    return int(st,2)

# 3) https://www.codewars.com/kata/58ce8725c835848ad6000007/train/python
def potatoes(p0, w0, p1):
    return w0 *(100-p0) // (100-p1)

# 4) https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python
def arithmetic(a, b, op):
    if op == 'add':
        return a+b
    elif op == 'subtract':
        return a-b
    elif op == 'multiply':
        return a*b
    elif op == 'divide':
        return a/b

# 5) https://www.codewars.com/kata/675dc1d3830826975c58a09d/train/python
def generate_C(size):
    res = []
    f_l = []
    for _ in range(size):
        f_l.append('C' * (5 * size))
    for _ in range(size * 3):
        res.append('C' * size)
    res = f_l + res + f_l
    
    return '\n'.join(res)

# 6) https://www.codewars.com/kata/56f253dd75e340ff670002ac/train/python
def compose(s1, s2):
    s1 = s1.split("\n")
    s2 = s2.split("\n")
    return '\n'.join([s1[i][:i+1] +s2[len(s2) -1 -i][:len(s2) - i] for i in range(len(s1))])

# 7) https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python
def small_enough(array, limit):
    return True if max(array) <= limit else False

# 8) https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Input must be between 0 and 12 (inclusive)")
    factorial = 1
    for i in range(n):
        factorial *= n - i
    return factorial

# 9) https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
def dont_give_me_five(start,end):
    nums = []
    for i in range(start,end+1):
        if not '5' in str(i):
            nums.append(i)
    return len(nums)

# 10) https://www.codewars.com/kata/526c7363236867513f0005ca/train/python
def is_leap_year(year):
    if year % 4 == 0 and not year % 100 == 0 :
        return True
    elif year % 100 == 0 and not year % 400 == 0:
        return False
    elif year % 400 == 0 :
        return True
    else:
        return False