listi = [1,2,3,4,5,6,7,8,9]
def myfunc(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(list(map(myfunc,listi)))