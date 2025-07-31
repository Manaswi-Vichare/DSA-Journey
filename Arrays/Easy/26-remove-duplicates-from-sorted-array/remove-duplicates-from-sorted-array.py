#dsajourney-MV
#Better Approach:
class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

#First Approach:
# class Solution(object):
#     def removeDuplicates(self, nums):
#         k = 1
#         i = 1
#         n = len(nums)
#         while i < n:
#             if nums[i] == nums[i-1]:
#                 value = nums[i]
#                 nums.pop(i)
#                 nums.append(value)
#                 n -= 1
#             else:
#                 i += 1
#                 k += 1
#         return k
