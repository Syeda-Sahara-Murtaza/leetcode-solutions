1
2# Definition for a binary tree node.
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution:
9    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
10        result = []
11
12        def inorder(node):
13            if node is None:
14                return
15
16            inorder(node.left)
17            result.append(node.val)
18            inorder(node.right)
19
20        inorder(root)
21        return result