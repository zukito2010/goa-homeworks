def bin_to_dec(n):
    strn = str(n)
    res = [] 
    for i, j in zip(range(len(strn)), range(len(strn) - 1, -1, -1)):
        res.append(int(strn[i])*(2**j))
    return sum(res)

print(bin_to_dec(110))

def dec_to_bin(n): 
    res = [] 
    while n > 0: 
        res.append(str(n % 2)) 
        n //= 2 
    return ''.join(res[::-1])

print(dec_to_bin(6))

# https://www.codewars.com/kata/59fca81a5712f9fa4700159a/train/python
def to_binary(n):
    res = [] 
    while n > 0: 
        res.append(str(n % 2)) 
        n //= 2 
    return int(''.join(res[::-1]))
