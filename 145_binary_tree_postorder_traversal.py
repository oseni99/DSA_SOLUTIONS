# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # for the post order it moves from left to right to root
        # we use two stack and use the dfs for the root left right
        if not root:
            return []
        stack_1 = [root]  # the dfs
        stack_2 = []  # this is what i use to reverse it
        curr = root
        while stack_1:
            curr = stack_1.pop()
            stack_2.append(curr.val)
            if curr.left:
                stack_1.append(curr.left)
            if curr.right:
                stack_1.append(curr.right)
        res = [i for i in reversed(stack_2)]
        return res