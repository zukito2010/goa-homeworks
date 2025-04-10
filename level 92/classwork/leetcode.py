# 1)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         for i in range(1,len(nums)):
#             if nums[i] - nums[i-1] == 1:
#                 continue
#             else:
#                 return nums[i]-1
#         return nums[0]-1 if not 0 in nums else nums[-1]+1 if nums[-1] in nums else nums[-1]

# 2)
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         return s.reverse()
        

# 3)
# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [[p,s] for p,s in zip(position,speed)]

#         stack = []
#         for p,s in sorted(pair)[::-1]:
#             stack.append((target - p) / s)
#             if len(stack) >= 2 and stack[-1] <= stack[-2]:
#                 stack.pop()
#         return len(stack)
