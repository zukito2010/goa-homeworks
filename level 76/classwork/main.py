import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def gcd_matrix(a,b):
    res = []
    ab = a+b
    divs = list(divisorGenerator(min(ab)))
    for x in range(len(divs)):
        for i in ab:
            if i % divs(-x) :
                res.append()
            else:
                break
        if len(res) == len(ab):
            return res[0]
        
    
    
    
print(list(divisorGenerator(100)))
print(gcd_matrix([1,2,3],[4,5,6]))