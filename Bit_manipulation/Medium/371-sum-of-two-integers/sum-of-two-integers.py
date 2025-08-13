#dsajourney-MV
class Solution(object):
    def getSum(self, a, b):
        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
        