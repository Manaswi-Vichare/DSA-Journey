#dsajourney-MV
#W/O In-built functions
class Solution(object):
    def reverseWords(self, s):
        i = 0
        n = len(s)
        res = ''
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            j = i + 1
            while j < n and s[j] != ' ':
                j += 1
            sub = s[i : j]
            if len(res) == 0:
                res = sub
            else:
                res = sub + " " + res
            i = j + 1
        return res

#With In-built functions
# class Solution(object):
#     def reverseWords(self, s):
#         words = s.split()
#         reversed_words = words[::-1]
#         result = " ".join(reversed_words)
#         return result            