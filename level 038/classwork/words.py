def sentence(*words):
    words = list(words)
    stri = []
    for word in words:  
        stri.append(word) 
    return ' '.join(stri)

print(sentence("mari ", "aris ", "kai ", "bavshvi"))