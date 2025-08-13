#dsajourney-MV
#BIT MANIPULATION - TC: O(N), SC: O(1)
class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        
        set_bit = xor & -xor
    
        i, j = 0, 0
        for num in nums:
            if num & set_bit:
                i ^= num
            else:
                j ^= num
        return [i, j]


#FREQUENCY MAP - TC, SC: O(N)
# class Solution(object):
#     def singleNumber(self, nums):
#         freq = defaultdict(int)
#         for n in nums:
#             freq[n] += 1
#             print(n, freq[n])
#         res = []
#         for num, f in freq.items():
#             if f == 1:
#                 res.append(num)
#         return res

#BRUTE-FORCE - TC: O(N^2), SC: O(1)
# class Solution(object):
#     def singleNumber(self, nums):
#         i, j = 0, 0
#         result = []
#         for i in range(len(nums)):
#             duplicate = False
#             for j in range(len(nums)):
#                 if nums[i] == nums[j] and i != j:
#                     duplicate = True
#                     break
#             if not duplicate:
#                 result.append(nums[i])
#         return result