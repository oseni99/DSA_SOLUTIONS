# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal is a bfs
        # for a bfs you need a queue
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            levels_res = []
            levels = len(queue)
            for _ in range(levels):
                curr = queue.popleft()
                levels_res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(levels_res)
        return res