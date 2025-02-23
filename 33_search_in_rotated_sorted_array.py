class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first thing i should do is find that position where it changes
        # because if its sorted the position where it changes from high to low is where it changes
        # where it goes from the largest to smallest is where it rotates

        def find_pivot(arr):
            l = 0
            r = len(arr) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        # after seeing where it changes
        # if pivot is greater than number then its left side else right side
        # this allows us to know where to run the binary search in

        def binary_search(arr, l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        pivot_idx = find_pivot(nums)
        l = 0
        r = len(nums) - 1
        # i know that if i my smallest is smaller than right starughtaway then its not rotated
        if nums[l] < nums[r]:
            return binary_search(nums, l, r)
        # what i now use to check where to do the bs is if its greater or equal to the first one or it isnt 
        if target >= nums[0]:
            return binary_search(nums, l=0, r=pivot_idx - 1)
        else:
            return binary_search(nums, l=pivot_idx, r=len(nums) - 1)