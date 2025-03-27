# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # i will just basically check if once i see root of the sub root in the first one
        #  i keep checking and if original now exists and sub root is at end
        # i return false at that point
        def sametree(x, y):
            if not x and not y:
                return True
            if not x or not y or x.val != y.val:
                return False
            return sametree(x.left, y.left) and sametree(x.right, y.right)

        def has_subtree(root):
            if not root:
                return False
            if sametree(root, subRoot):
                return True
            return has_subtree(root.left) or has_subtree(root.right)

        return has_subtree(root)