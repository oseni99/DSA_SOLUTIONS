# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # basically its just me validating what a bst is
        # i have to check

        def dfs(root, left_node, right_node):
            if not root:
                return True

            if root.val >= right_node or root.val <= left_node:
                return False
            return dfs(root.left, left_node, root.val) and dfs(
                root.right, root.val, right_node
            )

        return dfs(root, float("-inf"), float("inf"))