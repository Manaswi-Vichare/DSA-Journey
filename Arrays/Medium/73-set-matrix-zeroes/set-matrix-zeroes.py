#dsajourney-MV
#TC: O(M*N); SC: O(M+N)
class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        rows_to_zero = set()
        cols_to_zero = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        for i in rows_to_zero:
            matrix[i] = [0] * n
            print("2nd", i, j)

        for j in cols_to_zero:
            for i in range(m):
                matrix[i][j] = 0
        return matrix