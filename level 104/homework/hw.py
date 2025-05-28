# 1)
def sortme(words):
    return sorted(words, key=str.lower)

# 2)
def count(s):
    # The function code should be here
    return {i:s.count(i) for i in set(s)}
# 3)
def highest_rank(arr):
    setarr = set(arr)
    nums = []
    for i in setarr:
        nums.append([arr.count(i),i])
    return list(setarr)[nums.index(max(nums))]