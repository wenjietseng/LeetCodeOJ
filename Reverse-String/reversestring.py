class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[-1::-1] # a list object with slice [start:end:follow some order]
