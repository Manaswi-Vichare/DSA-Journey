#dsajourney-MV
#TC: O(N^2); SC: O(1)
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        l = 0
        r = len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
            
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix