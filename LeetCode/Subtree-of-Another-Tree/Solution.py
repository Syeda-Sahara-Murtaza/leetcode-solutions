1class Solution:
2    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
3        if p is None and q is None:
4            return True
5        if p is None or q is None or p.val != q.val:
6            return False
7        return self.isSameTree(p.left, q.left) and \
8               self.isSameTree(p.right, q.right)
9    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
10        if subRoot is None:
11            return True
12        if root is None:
13            return False
14        if self.isSameTree(root, subRoot):
15            return True
16        return self.isSubtree(root.left, subRoot) or \
17               self.isSubtree(root.right, subRoot)
18
19
20
21               
22# Definition for a binary tree node.
23# class TreeNode:
24#     def __init__(self, val=0, left=None, right=None):
25#         self.val = val
26#         self.left = left
27#         self.right = right