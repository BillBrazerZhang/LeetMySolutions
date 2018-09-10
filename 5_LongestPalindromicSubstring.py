class Solution(object):
    def DP_longestCommonSubstring(a, b):
        """
        :type a, b: str
        """
        L = []
        for i in range(len(a)):
            L.append([])
            for j in range(len(b)):
                L[i].append(0)
        z = 0
        ret = ""
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    if i == 0 or j == 0:
                        L[i][j] = 1
                    else:
                        L[i][j] = L[i-1][j-1] + 1
                    if L[i][j] > z:
                        z = L[i][j]
                        ret = a[i-z+1 : i+1]
                else:
                    L[i][j] = 0
        return {'maxLen':z, 'maxStr':ret}

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s
        b = ""
        for i in range(len(a)):
            b += a[len(a)-i-1]

        L = []
        for i in range(len(s)):
            L.append([])
            for j in range(len(s)):
                L[i].append(0)
        z = 0
        ret = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if a[i] == b[j]:
                    if i == 0 or j == 0:
                        L[i][j] = 1
                    else:
                        L[i][j] = L[i-1][j-1] + 1
                    if L[i][j] > z and i+j-L[i][j]+1 == len(s)-1:
                        z = L[i][j]
                        ret = a[i-z+1 : i+1]
                else:
                    L[i][j] = 0
        return ret
