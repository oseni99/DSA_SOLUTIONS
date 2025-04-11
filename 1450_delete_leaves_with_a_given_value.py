# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # find the target and this makes sense to do using the post order
        # we visit the child before the parent as thats the best way 

        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val == target and not root.left and not root.right:
                return None

            return root

        return dfs(root)