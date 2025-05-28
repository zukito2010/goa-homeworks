# 1)
def format_money(amount):
    if type(amount) is int:
        return f'${amount}.00'
    elif len(str(amount).split('.')[1]) == 1:
        return f'${amount}0'
    else:
        return f'${amount}'
    
