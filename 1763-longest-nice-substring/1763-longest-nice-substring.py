class Solution:
    def longestNiceSubstring(self, s):

        if len(s) < 2:
            return ""

        chars = set(s)

        for i in range(len(s)):
            if s[i].lower() in chars and s[i].upper() in chars:
                continue

            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i + 1:])

            if len(left) >= len(right):
                return left
            else:
                return right

        return s