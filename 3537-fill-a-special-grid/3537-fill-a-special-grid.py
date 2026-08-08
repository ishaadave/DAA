class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        size = 1 << n
        grid = [[0] * size for _ in range(size)]

        value = 0

        def solve(row, col, length):
            nonlocal value

            if length == 1:
                grid[row][col] = value
                value += 1
                return

            half = length // 2

            # Top-right
            solve(row, col + half, half)

            # Bottom-right
            solve(row + half, col + half, half)

            # Bottom-left
            solve(row + half, col, half)

            # Top-left
            solve(row, col, half)

        solve(0, 0, size)

        return grid