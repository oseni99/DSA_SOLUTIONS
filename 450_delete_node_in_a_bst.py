# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # i find the node and i know since its a BST its going to be one side
        #  once i find that node i swap it with the minimum node and delete the minimum node
        def find_min(root):
            # it is going to be at the left side
            while root.left:
                root = root.left
            return root

        #  if no root
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # if i want to delete a node 3 occurence
            #  if its one child or its two child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # the complex case of two child and i replace with min node
                min_node = find_min(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root