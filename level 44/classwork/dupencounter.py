def duplicate_encode(word):
    res = [] #result list
    word = word.lower()  #make words lower to not be case sensitive
    for i in word:
        if word.count(i) == 1: #check if symbol appears once 
            res.append('(') #append ( in res if symbol appears once
        else:
            res.append(')') #else append )
    return ''.join(res) #making it from list to string