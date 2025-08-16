#dsajourney-MV
class Solution(object):
    def zeroFilledSubarray(self, nums):
        count, streak = 0, 0
        for i in nums:
            if i == 0:
                streak += 1
                count += streak  
            else:
                streak = 0
        return count