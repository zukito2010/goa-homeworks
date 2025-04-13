# # 1)
# class Solution:
#     def reverse(self, x: int) -> int:
#         strx = str(x)
#         min_int = -2 ** 31
#         max_int = 2**31 -1
#         if x <= min_int or x >= max_int:
#             return 0
#         a = ''
#         for i in strx:
#             if i.isdigit():
#                 a += i
        
#         return int('-' + a[::-1]) if '-' in strx else int(a[::-1])
        

# # 2)
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.rstrip().split(' ')[-1])

# # 3)
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ''
        
#         a = strs[0]

#         for i in strs[1::]:
#             x = 0
#             while x < len(a) and x < len(i) and a[x] == i[x]:
#                 x += 1
#             a = a[0:x]
#             if a =='':
#                 break
#         return a