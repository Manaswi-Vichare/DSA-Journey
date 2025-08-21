#dsajourney-MV
#TC: O(n); SC: O(n)
class Solution(object):
    def findDuplicates(self, nums):
        seen = set()  
        output = []
        
        for i in nums:
            if i in seen:
                output.append(i) 
            else:
                seen.add(i) 
        return output