import random
from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:

        ans = []

        for k, trim in queries:

            arr = [(num[-trim:], i) for i, num in enumerate(nums)]
            target = k - 1

            def partition(left, right):
                pivot = arr[right]
                i = left

                for j in range(left, right):
                    if arr[j] <= pivot:
                        arr[i], arr[j] = arr[j], arr[i]
                        i += 1

                arr[i], arr[right] = arr[right], arr[i]
                return i

            def quickSelect(left, right):
                if left >= right:
                    return

                pivotIndex = random.randint(left, right)
                arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]

                p = partition(left, right)

                if p == target:
                    return
                elif p < target:
                    quickSelect(p + 1, right)
                else:
                    quickSelect(left, p - 1)

            quickSelect(0, len(arr) - 1)

            ans.append(arr[target][1])

        return ans