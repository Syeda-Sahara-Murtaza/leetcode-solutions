1class Solution:
2    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
3        diameter = 0
4        def height(node):
5            nonlocal diameter
6            if node is None:
7                return 0
8            left = height(node.left)
9            right = height(node.right)
10            # Longest path passing through this node
11            diameter = max(diameter, left + right)
12            # Return height of this node
13            return 1 + max(left, right)
14        height(root)
15        return diameter
16
17
18
19
20
21
22
23        # Definition for a binary tree node.
24# class TreeNode:
25#     def __init__(self, val=0, left=None, right=None):
26#         self.val = val
27#         self.left = left
28#         self.right = right