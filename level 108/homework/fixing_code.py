# code to fix:
def calculate(n1, n2, op):
    match op:
        case "+": return n1 + n2
        case "-": return n1 - n2
        case "*": return n1 * n2
    return n1 / n2

def calc(expr):
    if not expr: return 0
    arr = []
    
    for i in expr.split():
        if i.isdigit():
            arr.append(int(i))
        else:
            res = calculate(arr[-2], arr[-1], i)
            if len(arr) > 2:
                arr = arr[:-2] + [res]
            else:
                arr = [res]
    return arr[0]

# 6 kyu I
def sortme(words):
    return sorted(words, key=str.lower)

# 6 kyu II
def reverse_alternate(st):
    st = st.split()
    res = []
    for i in range(0,len(st)):
        if i % 2 == 0:
            res.append(st[i])
        else:
            res.append(st[i][::-1])
    
    
    return ' '.join(res).strip()
        