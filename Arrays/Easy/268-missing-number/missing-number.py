#dsajourney-MV
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        arr = sorted(nums)
        if arr[-1] != n:
            return n
        elif arr[0] != 0:
            return 0
        else: 
            for i in range(1, n):
                if arr[i] - arr[i-1] != 1:
                    miss = arr[i] - 1
                    print(miss)
                    return miss