class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0] * n
        # add each num into a new array by k places
        for i in range(n):
            idx = (i + k) % n
            res[idx] = nums[i]
        #  now put it back inside by copying it inside
        for i in range(n):
            nums[i] = res[i]