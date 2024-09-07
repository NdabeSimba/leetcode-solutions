# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # 2
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root

    # 3
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            left = root.left
            right = root.right

            root.left = right
            root.right = left

            self.invertTree(root.left)
            self.invertTree(root.right)

            return root
