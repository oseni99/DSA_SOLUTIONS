# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #  what i know about the right side is that its using a bfs
        #  the last one in my bfs is the right side
        res = []
        if not root:
            return []
        queue = deque([root])
        while queue:
            levels = len(queue)
            for _ in range(levels):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr.val)
        return res