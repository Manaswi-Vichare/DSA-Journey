class Solution(object):
    def hammingWeight(self, n):
        b = bin(n)[2:]
        print(b)
        print(len(b))
        count = 0
        for i in range(0, len(b)):
            if b[i] == '1':
                count += 1
        return count