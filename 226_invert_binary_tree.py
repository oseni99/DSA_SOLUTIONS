# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # basically the inverting the tree is just swapping the left for the right nodes
        if root:
            root.left, root.right = root.right, root.left

            # this now recursively does it for left side and right side
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root