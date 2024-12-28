def is_cooked(func):    
    def cooking():
        print('Your meal is cooked now')
        func()
        
    return cooking



@is_cooked
def raw_beef():
    print('eating beef')

raw_beef()