class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        import string
        from collections import defaultdict
        rows = defaultdict(str)
        if numRows == 1:
            return s
        for i in range(len(s)):
            remainder = i % (2*numRows-2)
            if  remainder < numRows:
                rows[remainder] += s[i]
            else:
                rows[2*numRows-2 - remainder] += s[i]
        zigZag = ''
        for j in range(numRows):
                zigZag += rows[j]
        return zigZag