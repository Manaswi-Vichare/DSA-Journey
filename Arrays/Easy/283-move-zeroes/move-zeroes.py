#dsajourney-MV
#Follow up Q - Avoiding self swaps - TC: O(n); SC: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1

#Array - TC: O(n); SC: O(1)
# class Solution(object):
#     def moveZeroes(self, nums):
#         i = 0
#         for j in range(len(nums)):
#             if nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1