#dsajourney-MV
class Solution(object):
    def zeroFilledSubarray(self, nums):
        n = len(nums)
        i = 0
        count, streak = 0, 0
        while i < n:
            if nums[i] == 0:
                streak += 1
                count += streak  
            else:
                streak = 0
            i += 1 
        return count