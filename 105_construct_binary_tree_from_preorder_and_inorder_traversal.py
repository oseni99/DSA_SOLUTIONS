# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #  i know that pre order is root left right so everything inside the preorder is always a root
        # i know that inorder for each root to the left is left node and to the right is right node
        # so i have to pick that pre order root check it inside inorder
        if not preorder or not inorder:
            return None
        dummy = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        dummy.left = self.buildTree(preorder[1: idx + 1], inorder[: idx])
        dummy.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return dummy