# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # i think to do this i should just do an inorder traversal and return the kth one first
        self.res = []

        def inorder(root):
            if not root:
                return
            # left root right
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)

        inorder(root)
        return self.res[k - 1]