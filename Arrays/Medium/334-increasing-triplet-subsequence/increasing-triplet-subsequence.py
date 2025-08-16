#dsajourney-MV
class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')
        if len(nums) < 3:
            return False
            
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
