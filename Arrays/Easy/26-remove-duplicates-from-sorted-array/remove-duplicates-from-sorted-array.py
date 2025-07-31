#dsajourney-MV
class Solution(object):
    def removeDuplicates(self, nums):
        # k = 1
        # i = 1
        # n = len(nums)
        # while i < n:
        #     if nums[i] == nums[i-1]:
        #         value = nums[i]
        #         nums.pop(i)
        #         nums.append(value)
        #         n -= 1
        #     else:
        #         i += 1
        #         k += 1
        # return k
        if not nums:
            return 0
        
        k = 1  

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  
                nums[k] = nums[i]
                k += 1

        return k
