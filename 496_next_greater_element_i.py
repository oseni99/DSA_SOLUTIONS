class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # i have to use a stack
        # monotonic stack and i use it to find whats greater each time
        # i can also create a hashmap that holds number and its greater
        res = {}
        mono_stack = []
        for num in nums2:
            while mono_stack and mono_stack[-1] < num:
                idx = mono_stack.pop()
                res[idx] = num
            mono_stack.append(num)
        # this will also have some elements left so i just change that to -1 cuz no nex greater
        for i in mono_stack:
            res[i] = -1
        return [res[i] for i in nums1]