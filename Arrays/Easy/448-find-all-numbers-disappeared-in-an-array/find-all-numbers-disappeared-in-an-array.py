#dsajourney-MV
#Follow up - TC: O(n); SC: O(1)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
