class Solution:
    def searchMatrix(self, matrix, target):

        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        def search(top, bottom, left, right):

            if top > bottom or left > right:
                return False

            if target < matrix[top][left] or target > matrix[bottom][right]:
                return False

            mid = (left + right) // 2

            row = top
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search(row, bottom, left, mid - 1) or \
                   search(top, row - 1, mid + 1, right)

        return search(0, rows - 1, 0, cols - 1)