# 1) https://www.codewars.com/kata/55acfc59c3c23d230f00006d/train/python
def get_ascii(ch : str) -> int:
    return ord(ch)

# 2) https://www.codewars.com/kata/55ccdf1512938ce3ac000056/train/python
def is_loch_ness_monster(string):
    if 'tree fiddy' in string or 'three fifty' in string or '3.50' in string:
        return True
    else:
        return False

# 3) https://www.codewars.com/kata/55eea63119278d571d00006a/train/python
def next_id(arr):
    unique_ids = set(arr)
    current_id = 0
    while True:
        if current_id not in unique_ids:
            return current_id
        current_id += 1

# 4) https://www.codewars.com/kata/582dafb611d576b745000b74/train/python
def quote(fighter):
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!" if fighter.lower() == 'conor mcgregor' else "I am not impressed by your performance."

# 5) https://www.codewars.com/kata/568018a64f35f0c613000054/train/python
class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
    def guess(self,n):
        if self.lives == 0:
            raise 'Omae wa mo shindeiru'
        elif n == self.number:
            return True
        else:
            self.lives -= 1
            return False

# 6) https://www.codewars.com/kata/588417e576933b0ec9000045/train/python
def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_rows - row) * (tot_cols - col +1)

# 7) https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python
def validate_hello(greetings):
    greets = ['hello','ciao','salut','hallo','hola','ahoj','czesc']
    for i in greets:
        if i in greetings.lower():
            return True
    return False

# 8) https://www.codewars.com/kata/55c933c115a8c426ac000082/train/python
def eval_object(v):
    match v["operation"]:
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 1

# 9) https://www.codewars.com/kata/562926c855ca9fdc4800005b/train/python
def number_to_pwr(number, p):
    a = 1
    for i in range(p):
        a*=number
    return a

# 10) https://www.codewars.com/kata/5748a883eb737cab000022a6/train/python
def cannons_ready(gunners):
    if 'nay' in gunners.values():
        return 'Shiver me timbers!'
    else:
        return 'Fire!'

# 11) https://www.codewars.com/kata/57613fb1033d766171000d60/train/python
def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
    elif scores[0] == scores[1]:
        return f'At match {teams[0]} - {teams[1]}, teams played draw.'
    return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"

# 12) https://www.codewars.com/kata/563c13853b07a8f17c000022/train/python
from datetime import datetime

def is_today(date: datetime) -> bool:
    return date.date() == datetime.today().date()

# 13) https://www.codewars.com/kata/5601c5f6ba804403c7000004/train/python
def bar_triang(point_a, point_b, point_c): 
    xO = round((point_a[0] + point_b[0] + point_c[0]) / 3, 4)
    yO = round((point_a[1] + point_b[1] + point_c[1]) / 3, 4)
    return [xO, yO]

# 14) https://www.codewars.com/kata/559f80b87fa8512e3e0000f5/train/python
odds = lambda lst: [x for x in lst if x % 2 == 1]

# 15) https://www.codewars.com/kata/56a25ba95df27b7743000016/train/python
def validate_code(code):
    nums = ['1','2','3']
    if str(code)[0] in nums:
        return True
    else:
        return False

# 16) https://www.codewars.com/kata/56fcfad9c7e1fa2472000034/train/python
def evil(n):
    a = bin(n).count('1')
    return "It's Evil!" if a % 2 == 0 else "It's Odious!"