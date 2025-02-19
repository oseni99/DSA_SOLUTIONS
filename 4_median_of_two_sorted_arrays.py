class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        new_arr = sorted(arr)
        n = len(new_arr)
        a = n // 2
        if n % 2 == 0:
            return (new_arr[a - 1] + new_arr[a]) / 2
        return new_arr[a]