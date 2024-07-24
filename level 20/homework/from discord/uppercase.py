def upper_caser(string):
    result = ""
    for i in range(len(string)): 
        if i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i].lower()
    print(result)



upper_caser("mamasheni")
