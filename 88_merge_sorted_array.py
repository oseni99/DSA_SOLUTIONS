class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m - 1
        r = n - 1
        i = len(nums1) - 1
        while r >= 0 and l >= 0:
            if nums1[l] < nums2[r]:
                nums1[i] = nums2[r]
                r -= 1
            else:
                nums1[i] = nums1[l]
                l -= 1
            i -= 1
        # this handles lets say every element is bigger than the r e.g [4,5,6] [1,2,3]
        while r >= 0:
            nums1[i] = nums2[r]
            r -= 1
            i -= 1