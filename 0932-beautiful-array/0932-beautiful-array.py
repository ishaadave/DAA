class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def solve(n):

            if n == 1:
                return [1]

            left = solve((n + 1) // 2)
            right = solve(n // 2)

            ans = []

            for x in left:
                ans.append(2 * x - 1)

            for x in right:
                ans.append(2 * x)

            return ans

        return solve(n)