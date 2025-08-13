#dsajourney-MV
class Solution(object):
    def singleNumber(self, nums):
        i, j = 0, 0
        result = []
        for i in range(len(nums)):
            duplicate = False
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    duplicate = True
                    break
            if not duplicate:
                result.append(nums[i])
        return result
