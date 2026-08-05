import random

class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while True:
            pivot = nums[random.randint(left, right)]

            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return nums[target]