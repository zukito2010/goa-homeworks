def manual_startswith(st,word):
    x = st[0:len(word)]
    return word == x

print(manual_startswith('hello guys','hello'))
print(manual_startswith('hello guys','bello'))