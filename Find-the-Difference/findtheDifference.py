class Solution(object):
    def findTheDifference(self, s, t):
        """
        # ord difference
        s_ord = 0
        t_ord = 0
        for ch in s:
            s_ord += ord(ch)
        for ch in t:
            t_ord += ord(ch)
        return chr(t_ord - s_ord)
        """
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)
