class Solution:
    def majorityElement(self, nums):

        def solve(left, right):

            if left == right:
                return nums[left]

            mid = (left + right) // 2

            leftMajor = solve(left, mid)
            rightMajor = solve(mid + 1, right)

            if leftMajor == rightMajor:
                return leftMajor

            leftCount = nums[left:right + 1].count(leftMajor)
            rightCount = nums[left:right + 1].count(rightMajor)

            if leftCount > rightCount:
                return leftMajor
            else:
                return rightMajor

        return solve(0, len(nums) - 1)