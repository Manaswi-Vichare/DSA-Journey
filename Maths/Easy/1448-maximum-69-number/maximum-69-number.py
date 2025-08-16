#dsajourney-MV
class Solution(object):
    def maximum69Number (self, num):
        arr = map(int, str(num))
        for i in range(0, len(arr)):
            if arr[i] == 6:
                arr[i] = 9
                break
        num = int("".join(map(str, arr)))
        return num