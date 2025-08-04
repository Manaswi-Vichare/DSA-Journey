#dsajourney-MV
#Using in-built function
class Solution(object):
    def isPalindrome(self, s):
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        return new_s == new_s[::-1]



#First approach
# import math
# import re
# class Solution(object):
#     def isPalindrome(self, s):
#         i, j = 0, 0
#         front, back = 0, 0
#         s = s.lower()
#         s = s.replace(" ", "")
#         s = re.sub(r'[^a-zA-Z0-9]', '', s)
#         if len(s) == 1 or len(s) == 0:
#             return True          

#         half = int(math.floor(len(s)/2))
#         while i < half and j < half:
#             for i in range(0, half):
#                 for j in range(len(s) - 1, half - 1, -1):
#                     if s[i] != s[j]:
#                         return False
#                     else:
#                         i += 1
#                 return True