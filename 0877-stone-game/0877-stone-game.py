class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        memo = {}

        def solve(left, right):

            if left == right:
                return piles[left]

            if (left, right) in memo:
                return memo[(left, right)]

            takeLeft = piles[left] - solve(left + 1, right)
            takeRight = piles[right] - solve(left, right - 1)

            memo[(left, right)] = max(takeLeft, takeRight)

            return memo[(left, right)]

        return solve(0, len(piles) - 1) > 0