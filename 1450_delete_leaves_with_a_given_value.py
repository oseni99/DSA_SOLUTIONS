# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        #  what im thinking is i go through my tree and once i see that theres no more node
        # i check if its target and if its target i delete it
        # its only going to be like one node which is one case
        # a dfs
        if not root:
            return None

        # i now recursively call it for both left and right
        # to delete a leaf node we use a post order traversal
        # find the parent since its left right root we visit child before parent 
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            # if no one i just delete that node
            return None
        return root