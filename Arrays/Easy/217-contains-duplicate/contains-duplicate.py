#dsajourney-MV
class Solution(object):
    def containsDuplicate(self, nums):
        i, count = 0, 0
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
        if count >= 1 and len(nums) > 1:
            return True
        else:
            return False