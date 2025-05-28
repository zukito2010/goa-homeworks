# 
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }
#         res = 0
#         prev = 0

#         for i in s[::-1]:
#             current = roman[i]
#             if current < prev:
#                 res -= current
#             else:
#                 res += current
#             prev = current
#         return res

# # 2)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         res = 0
#         listn = []

#         for i in range(len(nums)):
#             if nums[i] != val:
#                 res += 1
#             else:
#                 listn.append(i)
        
#         for i in listn:
#             nums[i] = '_'
        
#         for i in range(nums.count("_")):
#             nums.remove("_")
        
#         return res

# 3)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         res = 0
#         listn = []

#         for i in range(len(nums)):
#             if nums[i] != val:
#                 res += 1
#             else:
#                 listn.append(i)
        
#         for i in listn:
#             nums[i] = '_'
        
#         for i in range(nums.count("_")):
#             nums.remove("_")
        
#         return res

# 4)
# class Solution:
#     def isValid(self, s: str) -> bool:
#         while '()' in s or '[]' in s or '{}' in s:
#             s = s.replace('()',"").replace('[]','').replace('{}','')
#         return not s

# 5)
# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         total = 0
#         for i in range(1,len(s)):
#             total += abs(ord(s[i]) - ord(s[i-1]))
#         return total