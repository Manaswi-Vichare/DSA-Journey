#dsajourney-MV
#TC: O(n); SC: O(1)
class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]
        return result

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

#TC: O(nlogn); SC: O(n)
class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        result=[]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                result.append(nums[i])
        return result
        