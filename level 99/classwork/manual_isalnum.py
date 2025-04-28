def manual_isalnum(n):
    alphanum = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
    try:
        for i in n:
            if i in alphanum:
                pass
            else:
                return False
            
        return True
    except TypeError:
        return 'Wrong type!'

print(manual_isalnum('sadsadbasda'))
print(manual_isalnum('*&%asdw'))
print(manual_isalnum(632))