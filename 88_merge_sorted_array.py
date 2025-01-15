class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = n - 1
        i = len(nums1) - 1
        # i want to start from the back
        #  check if that number before 0 is less than or greater than
        # since its sorted in increasimg order
        #  that i is what we use to insert it
        # TC of O(m+n)
        while a >= 0 and b >= 0:
            if nums1[a] <= nums2[b]:
                nums1[i] = nums2[b]
                b -= 1
            else:
                nums1[i] = nums1[a]
                a -= 1
            i -= 1
        #  case where i still have elements left inside the nums2
        while b >= 0:
            nums1[i] = nums2[b]
            b -= 1
            i -= 1