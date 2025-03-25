# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #  it can also be solved using bfs
        if not root:
            return 0
        queue = deque([(root, 1)])
        max_depth = 0
        # the bfs
        while queue:
            curr, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            # now going to the left and right and increase the depth by 1
            if curr.left:
                queue.append([curr.left, depth + 1])
            if curr.right:
                queue.append([curr.right, depth + 1])
        return max_depth