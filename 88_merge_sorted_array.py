class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #  let me say
        nums1[m:] = nums2

        def quicksort(arr):
            # do quick sort on this
            def partition(low, high):
                i = low - 1
                pivot = arr[high]
                for j in range(low, high):
                    if arr[j] <= arr[high]:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                return i + 1

            def quick_sort_recursive(low, high):
                if low < high:
                    piv_idx = partition(low, high)
                    quick_sort_recursive(low, piv_idx - 1)
                    quick_sort_recursive(piv_idx + 1, high)

            quick_sort_recursive(0, len(arr) - 1)

        quicksort(nums1)