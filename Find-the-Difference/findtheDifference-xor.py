class Solution(object):
    def findTheDifference(self, s, t):
        # xor parity A ^ A = 1
        diff = 0
        for ch in s + t:
            diff ^= ord(ch)
        return chr(diff)
