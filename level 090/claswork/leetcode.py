# 1)
# class Solution:
#     def twoSum(self, nums, target):
#         res = {}
#         for i, num in enumerate(nums):
#             needed_number = target - num
#             if needed_number in res:
#                 return [res[needed_number], i]
#             res[num] = i

# 2)
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]:
            
# 3)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# 4)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = []
#         seen = set()
#         for i in range(len(strs)):
#             if i in seen:
#                 continue
#             group = [strs[i]]
#             seen.add(i)
#             for x in range(i+1,len(strs)):
#                 if sorted(strs[i]) == sorted(strs[x]):
#                     group.append(strs[x])
#                     seen.add(x)
#             anagrams.append(group)
#         return anagrams