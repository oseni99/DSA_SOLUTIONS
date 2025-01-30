class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # i have to use a stack
        # monotonic stack and i use it to find whats greater each time
        res = [-1] * len(nums2)
        mono_stack = []
        for i, j in enumerate(nums2):
            while mono_stack and nums2[mono_stack[-1]] < j:
                idx = mono_stack.pop()
                res[idx] = j
            mono_stack.append(i)
        total_res = [-1] * len(nums1)
        for i, j in enumerate(nums1):
            if j in nums2:
                idx = nums2.index(j)
                total_res[i] = res[idx]
        return total_res