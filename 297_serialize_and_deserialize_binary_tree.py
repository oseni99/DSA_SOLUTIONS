# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # this will work for both BST and normal TREES
        self.res = []

        def preorder(root):
            if not root:
                self.res.append("#")
                return
            self.res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(self.res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.idx = 0

        def build_tree():
            if self.idx >= len(data) or data[self.idx] == "#":
                self.idx += 1
                return
            root = TreeNode(int(data[self.idx]))
            self.idx += 1
            root.left = build_tree()
            root.right = build_tree()
            return root

        return build_tree()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))