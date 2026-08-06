class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()

        half = (len(nums) + 1) // 2

        left = nums[:half][::-1]
        right = nums[half:][::-1]

        nums.clear()

        for i in range(len(right)):
            nums.append(left[i])
            nums.append(right[i])

        if len(left) > len(right):
            nums.append(left[-1])