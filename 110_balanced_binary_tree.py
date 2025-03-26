# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # basically its just creating a recursive function that i use to check if left and right <= 1
        # return false early as soon as i see one that is > 1
        def dfs(root):
            if not root:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            # check the diff
            if abs(left_depth - right_depth) > 1:
                return -1

            # i now calc the height here
            return 1 + max(left_depth, right_depth)

        return dfs(root) != -1