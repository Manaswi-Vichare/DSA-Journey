#dsajourney-MV
#HashSet Based - TC: O(n); SC: O(1)
class Solution(object):
    def containsDuplicate(self, nums):
        s_nums = set(nums)
        if len(nums) == len(s_nums):
            return False
        else:
            return True

#Array Based - TC: O(nlogn); SC: Best- O(1), Worst- O(n)
# class Solution(object):
#     def containsDuplicate(self, nums):
#         i, count = 0, 0
#         nums.sort()
#         for i in range(0, len(nums)):
#             if nums[i] == nums[i-1]:
#                 count += 1
#         if count >= 1 and len(nums) > 1:
#             return True
#         else:
#             return False