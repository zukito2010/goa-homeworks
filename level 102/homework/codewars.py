# 1)
def dig_pow(n, p):
    total = sum(int(digit) ** (p + i) for i, digit in enumerate(str(n)))
    return total // n if total % n == 0 else -1
# 2)
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

# 3)
def sort_array(source_array):
    odds = sorted([x for x in source_array if x % 2 != 0])
    result = []
    odd_index = 0
    for x in source_array:
        if x % 2 != 0:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(x)
    return result
