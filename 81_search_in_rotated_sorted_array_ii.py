class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # it is similar but i think it
        myarr = list(set(nums))
        print(myarr)

        def find_pivot(myarr):
            l = 0
            r = len(myarr) - 1
            while l < r:
                m = (l + r) // 2
                if myarr[m] > myarr[r]:
                    l = m + 1
                else:
                    r = m
            return l

        def binary_search(l, r):
            while l <= r:
                m = (l + r) // 2
                if myarr[m] == target:
                    return True
                elif myarr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False

        pivot_idx = find_pivot(myarr)
        l = 0
        r = len(nums) - 1

        # if nums[l] <= nums[r]:
        #     return binary_search(l, r)
        # what i now use to check where to do the bs is if its greater or equal to the first one or it isnt
        return binary_search(l=0, r=pivot_idx - 1) or binary_search(
            l=pivot_idx, r=len(myarr) - 1
        )