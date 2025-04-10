# 2)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         nums.sort()
#         longest = 1
#         current_streak = 1

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 if nums[i] == nums[i - 1] + 1:
#                     current_streak += 1
#                 else:
#                     longest = max(longest, current_streak)
#                     current_streak = 1

#         return max(longest, current_streak)
# 3)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))

