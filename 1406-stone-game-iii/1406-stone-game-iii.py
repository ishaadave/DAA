class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)
        memo = {}

        def solve(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            best = float("-inf")
            total = 0

            for j in range(3):
                if i + j < n:
                    total += stoneValue[i + j]
                    best = max(best, total - solve(i + j + 1))

            memo[i] = best
            return best

        score = solve(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"