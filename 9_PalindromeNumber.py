class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        s = str(x)
        l = len(x)

        for i in range(l/2+1):
            if s[i] != s[l-i-1]:
                return False

        return True
