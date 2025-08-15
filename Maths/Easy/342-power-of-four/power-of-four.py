#dsajourney-MV
class Solution(object):
    def isPowerOfFour(self, n):
        if n < 0 or n == 0:
            return False
        a = log(n) / log(4)
        if float(a).is_integer():
            return True
        else:
            return False