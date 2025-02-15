# Leetcode 125

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re

        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        pal = s[::-1]
        if s==pal:
            return True
        else:
            return False
        
