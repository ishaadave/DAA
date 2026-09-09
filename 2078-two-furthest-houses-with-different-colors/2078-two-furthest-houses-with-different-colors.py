class Solution:
    def maxDistance(self, colors):
        n = len(colors)

        # Check first house with houses from the right
        for j in range(n - 1, -1, -1):
            if colors[0] != colors[j]:
                ans1 = j
                break

        # Check last house with houses from the left
        for i in range(n):
            if colors[i] != colors[n - 1]:
                ans2 = n - 1 - i
                break

        return max(ans1, ans2)