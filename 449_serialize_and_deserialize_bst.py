# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    # the best way to do this is using a preorder traversal since it always has root
    # pre order is root to left to right
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        self.res = []

        def preorder(root):
            if not root:
                #  there might be some None nodes inside that tree so i have to take account of that
                self.res.append("#")
                return
            self.res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(self.res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        #  since i used a pre order it always has its root and easy to set
        new_data = data.split(",")
        self.idx = 0

        def build_tree():
            if self.idx >= len(new_data) or new_data[self.idx] == "#":
                self.idx += 1
                return
            root = TreeNode(int(new_data[self.idx]))
            self.idx += 1
            # now im recursively building that tree
            root.left = build_tree()
            root.right = build_tree()

            return root

        return build_tree()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans