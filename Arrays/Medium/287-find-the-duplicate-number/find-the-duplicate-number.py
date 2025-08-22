#dsajourney-MV
#Optimal Solution - Floyd's Tortoise and Hare Cycle Detection - TC: O(n); SC:O(1)
class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entry point
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

#TC: O(n); SC: O(n)
class Solution(object):
    def findDuplicate(self, nums):
        check = [False] * (len(nums)) 
    
        for n in nums:
            if check[n]:
                return n
            check[n] = True
        return -1