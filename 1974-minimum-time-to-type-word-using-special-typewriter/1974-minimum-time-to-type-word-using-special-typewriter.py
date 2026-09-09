class Solution:
    def minTimeToType(self, word):
        time = 0
        current = 'a'

        for ch in word:
            diff = abs(ord(ch) - ord(current))
            time += min(diff, 26 - diff) + 1
            current = ch

        return time