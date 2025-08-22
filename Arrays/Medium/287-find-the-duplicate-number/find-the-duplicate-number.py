#dsajourney-MV
#TC: O(n); SC: O(n)
class Solution(object):
    def findDuplicate(self, nums):
        check = [False] * (len(nums)) 
    
        for n in nums:
            if check[n]:
                return n
            check[n] = True
        return -1