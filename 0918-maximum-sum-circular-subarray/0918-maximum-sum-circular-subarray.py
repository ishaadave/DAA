class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total = sum(nums)

        maxSum = curMax = nums[0]
        minSum = curMin = nums[0]

        for num in nums[1:]:

            curMax = max(num, curMax + num)
            maxSum = max(maxSum, curMax)

            curMin = min(num, curMin + num)
            minSum = min(minSum, curMin)

        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)