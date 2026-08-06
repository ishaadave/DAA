import random
from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        target = len(nums) - k

        def less(a, b):
            if len(a) != len(b):
                return len(a) < len(b)
            return a < b

        def equal(a, b):
            return len(a) == len(b) and a == b

        def quickSelect(left, right):
            if left >= right:
                return nums[target]

            pivot = nums[random.randint(left, right)]

            lt = left
            i = left
            gt = right

            while i <= gt:
                if less(nums[i], pivot):
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif equal(nums[i], pivot):
                    i += 1
                else:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

            if target < lt:
                return quickSelect(left, lt - 1)
            elif target > gt:
                return quickSelect(gt + 1, right)
            else:
                return nums[target]

        return quickSelect(0, len(nums) - 1)