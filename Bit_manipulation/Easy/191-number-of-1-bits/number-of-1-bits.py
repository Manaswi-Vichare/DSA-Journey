#No in-built functions
class Solution(object):
    def hammingWeight(self, n):
        res = 0
        for i in range(32):
            if (n >> i) & 1:
                res += 1
        return res

#First Approach
# class Solution(object):
#     def hammingWeight(self, n):
#         b = bin(n)[2:]
#         print(b)
#         print(len(b))
#         count = 0
#         for i in range(0, len(b)):
#             if b[i] == '1':
#                 count += 1
#         return count