class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:

        m = len(matrix)
        n = len(matrix[0])

        pre = [[0] * (n + 1) for _ in range(m + 1)]
        values = []

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = (pre[i - 1][j] ^
                             pre[i][j - 1] ^
                             pre[i - 1][j - 1] ^
                             matrix[i - 1][j - 1])
                values.append(pre[i][j])

        values.sort(reverse=True)

        return values[k - 1]