# 1)
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return floor(x**0.5)

# 2)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
        # res = [x.lower() for x in s if x.isalnum()]
        # return res == res[::-1]

# 3)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return [x for x in set(nums) if nums.count(x) == 1][0]

# 4)
# class Solution:
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     a,b = 0,1
    #     for _ in range(2,n+1):
    #         a,b = b, a+b
    #     return b if n>0 else 
