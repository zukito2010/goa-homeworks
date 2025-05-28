# 1)
def highest_rank(arr):
    setarr = set(arr)#turn array to set
    nums = [] #creating empty list
    for i in setarr: 
        nums.append([arr.count(i),i])#getting every numbers rank
    return list(setarr)[nums.index(max(nums))] #returning highest rank
# 2)
def pos_average(s):
    list1 = s.split(', ')
    l = len(list1)
    sum = 0
    all_char = 0
    
    for i in range(l):
        for x in range(i + 1,l):
            for a,b in zip(list1[i],list1[x]):
                all_char += 1
                if a==b:
                    sum+=1
    return sum / all_char * 100
# 3)
def more_zeros(s):
    x = list(s)
    x = [bin(ord(i))[2:] for i in s]
    res = []
    indexes = []
    
    for i in range(len(x)):
        if x[i].count('0') > x[i].count('1'):
            indexes.append(i)
    
    for i in indexes:
        if s[i] not in res:
            res.append(s[i])
    
    return res