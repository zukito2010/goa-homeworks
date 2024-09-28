num = [163,567,73,43,2134,123,5422,15]

def evenify(x):
    if x % 2 == 1:
        return x+1
    else:
        return x

even_numbers = list(map(evenify,num))

print(even_numbers)


# map function takes two parameters function and an iterable and it makes function work on every element of the list in this case