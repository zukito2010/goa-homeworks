# 1) https://www.codewars.com/kata/52f3149496de55aded000410/train/python
def sum_digits(number):
    return eval('+'.join(list(str(abs(number)))))
    
# 2) https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python
def gimme(arr):
    sort_arr = sorted(arr)
    return arr.index(sort_arr[1])

# 3) https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python
def reverse_letter(st):
    res = ''
    for i in list(st)[::-1]:
        if i.isalpha():
            res += i
    
    return res

# 4) https://www.codewars.com/kata/5a03b3f6a1c9040084001765/train/python
def angle(n):
    return (n-2) * 180

# 5) https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python
import math

def round_to_next5(n):
    return 5 * math.ceil(n/5)

# 6) https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python
def two_oldest_ages(ages):
    sort_ages = sorted(ages)
    return [sort_ages[-2],sort_ages[-1]]

# 7) https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python
def capitalize(s):
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result.append(s[i].upper()) 
        else: 
            result.append(s[i].lower())  
    result2 = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result2.append(s[i].lower())  
        else: 
            result2.append(s[i].upper()) 
    return [''.join(result) , ''.join(result2) ]

# 8) https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/python
def no_odds(values):
    return [x for x in values if x % 2 == 0]
    
# 9) https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
def solve(s):
    lists = list(s)
    ups,downs = 0,0
    for i in lists:
        if i.isupper():
            ups += 1
        else:
            downs += 1
    return s.lower() if downs>=ups else s.upper() 

# 10) https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python
def check_exam(arr1,arr2):
    res = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            res += 4
        elif arr2[i] == '':
            res += 0
        else:
            res -= 1
    return 0 if res<0 else res
    