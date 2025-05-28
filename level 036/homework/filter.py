ages = [1,5,1,2,6,12,56,21,26,18]

def func(x):
    if x > 18:
        return True
    else:
        return False

adults = list(filter(func, ages))
print(adults)

# filter function is used to filter automatically instead of manually it takes two parameters, function and an iterable which it is going to filter


