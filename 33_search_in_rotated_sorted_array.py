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
        
        def binary_search(arr):
            l = 0
            r = len(arr) - 1
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
        if nums[pivot_idx] == target:
            return pivot_idx
        elif nums[pivot_idx] < target:
            return binary_search(nums[:pivot_idx])
        else:
            return binary_search(nums[pivot_idx:])