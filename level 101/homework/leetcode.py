# 1)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return [x for x in set(nums) if nums.count(x) == 1][0]

# 2)
# class Solution:
#     def generate(self, n: int) -> List[List[int]]:
#         triangle = []

#         for i in range(n):
#             row = [1]
#             if triangle:
#                 last_row = triangle[-1]
#                 row.extend(last_row[j] + last_row[j+1] for j in range(len(last_row) - 1))
#                 row.append(1)
#             triangle.append(row)
        
#         return triangle

# 3)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')
#         max_profit = 0

#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             profit = price - min_price
#             if profit > max_profit:
#                 max_profit=profit

#         return max_profit

# 4)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 profit += prices[i] - prices[i - 1]
#         return profit

# 5)
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         result = []

#         def is_palindrome(sub):
#             return sub == sub[::-1]

#         def backtrack(start, path):
#             if start == len(s):
#                 result.append(path[:])
#                 return
#             for end in range(start + 1, len(s) + 1):
#                 substring = s[start:end]
#                 if is_palindrome(substring):
#                     path.append(substring)
#                     backtrack(end, path)
#                     path.pop()

#         backtrack(0, [])
#         return result