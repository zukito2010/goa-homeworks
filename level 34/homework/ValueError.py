a = "abcdes"


try:
    print(float(a))    
except ValueError:
    print("ValueError found")