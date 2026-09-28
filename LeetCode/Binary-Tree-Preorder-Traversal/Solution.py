1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        result=[]
10        def preorder(node):
11            if node is None:
12                return
13            result.append(node.val)
14            preorder(node.left)
15            preorder(node.right)
16        preorder(root)
17        return result