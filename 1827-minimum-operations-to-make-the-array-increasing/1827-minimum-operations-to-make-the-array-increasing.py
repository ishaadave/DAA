class Solution:
    def minOperations(self, nums):
        operations = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1 - nums[i]
                operations += needed
                nums[i] += needed

        return operations