#dsajourney-MV
#Follow up Question - Gauss’ Sum Formula - TC: O(n); SC: O(1)
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = n * (n + 1) // 2
        actual = sum(n)
        return toal - sum

#Array based - TC: O(nlogn); SC: O(n)
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        arr = sorted(nums)
        if arr[-1] != n:
            return n
        if arr[0] != 0:
            return 0
        
        for i in range(1, n):
            if arr[i] - arr[i-1] != 1:
                miss = arr[i] - 1
                return miss