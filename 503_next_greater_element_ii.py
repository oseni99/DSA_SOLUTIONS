class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new_nums = nums * 2
        # find the next greater on this
        res = [-1] * len(new_nums)
        stack = []
        for i in range(len(new_nums)):
            while stack and new_nums[stack[-1]] < new_nums[i]:
                idx = stack.pop()
                res[idx] = new_nums[i]
            stack.append(i)
        return res[: len(nums)]