#dsajourney-MV
class Solution(object):
    def largestGoodInteger(self, num):
        if len(num) < 3:
            return ""

        count = 0
        res = ''
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count += 1
            else:
                count = 0

            if (count == 2):
                triple = num[i-2 : i+1]
                if res == "" or triple > res:
                    res = triple
        return res