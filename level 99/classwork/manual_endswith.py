def manual_endswith(st,word):
    x = st[-len(word):]
    return x == word

print(manual_endswith('this is a string','rang'))
print(manual_endswith('this is a string','ing'))