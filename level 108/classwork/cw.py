# 1)
def sort_sequence(sequence):
    result = []
    arr = []
    for i in sequence:
        if i != 0: arr.append(i)
        else:
            result.append(sorted(arr) + [0])
            arr = []
    return [x for i in sorted(result, key=sum) for x in i]

# 2)
def calc(expr):
    x = expr.split(' ')
    
    match x[-1]:
        case '+':
            return int(x[0]) + int(x[1])
        case '-':
            return int(x[0]) - int(x[1])
        case '*':
            return int(x[0]) * int(x[1])
        case '/':
            return int(x[0]) / int(x[1])
        case '':
            return 0
        case expr:
            if len(expr.split('.')) == 2:
                return float(x[-1])
            return int(x[-1])
# 3)