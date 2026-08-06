class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        arr = list(count.items())

        def quickSelect(left, right):
            if left >= right:
                return

            pivotIndex = random.randint(left, right)
            arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]

            pivot = arr[right][1]
            i = left

            for j in range(left, right):
                if arr[j][1] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[right] = arr[right], arr[i]

            if i == len(arr) - k:
                return
            elif i < len(arr) - k:
                quickSelect(i + 1, right)
            else:
                quickSelect(left, i - 1)

        quickSelect(0, len(arr) - 1)

        return [num for num, freq in arr[len(arr) - k:]]