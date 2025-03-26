# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # finding the diameter is just looking at the maximum from a point along its edges
        self.diameter = 0

        def dfs(root):
            if not root:
                return 0
            # i calculate the height at each of them and use it to determine the edges
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.diameter