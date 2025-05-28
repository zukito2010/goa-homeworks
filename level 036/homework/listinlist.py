nums = [[123,5422,15], [73,43,2134], [163,567,860] ]

def arithemtical(x):
    return sum(x) / len(x)

arith = list(map(arithemtical, nums))        
print(arith)



