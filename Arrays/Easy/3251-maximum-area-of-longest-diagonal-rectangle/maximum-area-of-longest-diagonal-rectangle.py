#dsajourney-MV
import math
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        m = len(dimensions)
        max_diag = 0
        
        for i in range(0, m):
            l = dimensions[i][0]
            b = dimensions[i][1]
            diag = math.sqrt(l * l + b * b)
            if diag > max_diag:
                max_diag = diag
                max_area = l * b
            elif diag == max_diag:
                max_area = max(max_area, l * b)
                
        return max_area
            
            