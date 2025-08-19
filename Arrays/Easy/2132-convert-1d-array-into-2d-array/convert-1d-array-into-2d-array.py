#dsajourney-MV
#TC: O(m*n); SC: O(1)
class Solution(object):
    def construct2DArray(self, original, m, n):
        res = []
        index = 0
        
        if m * n == len(original):
            for i in range(0, m):
                out = []
                for j in range(n):
                    out.append(original[index])
                    index += 1
                res.append(out)
            return res
        else:
            return []
        