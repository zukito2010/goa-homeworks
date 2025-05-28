# 1) https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
def number(bus_stops):
    res = 0
    for i in bus_stops:
        res += i[0] - i[1]
    return res

# 2) https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
def series_sum(n):
    if n == 0:
        return '0.00'
    res = 1
    a = 1
    for _ in range(n -1):
        a+=3
        res += 1 / a
    sol = str(round(float(res),2)) 
    
    return sol if len(sol) == 4 else sol+'0' 

# 3) https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python
def divisors(integer):
    divs = [i for i in range(2, integer) if integer % i == 0]
    
    if not divs:
        return f'{integer} is prime'
    
    return divs

# 4) https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
def divisors(integer):
    if integer == 1:
        return 1
    divs = [i for i in range(2, integer) if integer % i == 0]
    
    if not divs:
        return 2
    
    return len(divs) + 2

# 5) https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
def stray(arr):
    return [i for i in arr if arr.count(i) == 1][0]

# 6) https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python
def sequence_sum(beg, end, step):
    res = 0
    for i in range(beg,end+1,step):
        res += i
    return res

# 7) https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python
def sort_by_length(arr):
    return sorted(arr, key=len)

# 8) https://www.codewars.com/kata/566fc12495810954b1000030/train/python
def nb_dig(n, d):
    sqrs = []
    for i in range(1,n+1):
        sqrs.append(i*i)
    std = str(d)
    
    res = 0
    for i in sqrs:
        if std in str(i):
            res += str(i).count(std)
    return res+1 if d == 0 else res

# 9) https://www.codewars.com/kata/563f037412e5ada593000114/train/python
def calculate_years(P, I, T, D):
    years = 0
    while P < D:
        interest = P * I 
        taxed_interest = interest * (1 - T) 
        P += taxed_interest 
        years += 1  
    return years

# 10 https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
def capitals(word):
    caps = []
    for i in range(len(word)):
        if word[i].isupper():
            caps.append(i)
    
    return caps

