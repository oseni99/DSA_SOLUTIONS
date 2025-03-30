# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # i realized that to count good nodes it basically as we move down
        # we find a node if its >= to its root its a good node and add it to the res
        # as we go down we make the node the root for the next node
        self.res = 0

        def dfs(root, max_val):
            if not root:
                return
            if root.val >= max_val:
                self.res += 1
            # this is where i upload the new max value
            new_max_val = max(max_val, root.val)
            if root.left:
                dfs(root.left, new_max_val)
            if root.right:
                dfs(root.right, new_max_val)

        dfs(root, root.val)
        return self.res