1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val, prev, next, child):
5        self.val = val
6        self.prev = prev
7        self.next = next
8        self.child = child
9"""
10
11class Solution:
12    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
13        curr = head
14
15        while curr:
16            if curr.child:
17                child = curr.child
18                next_node = curr.next
19
20                # put child after curr
21                curr.next = child
22                child.prev = curr
23                curr.child = None
24
25                # find the end of child list
26                temp = child
27                while temp.next:
28                    temp = temp.next     # 1 2 3 7 8 9 10 4 5 6 
29                                                 # 11 12
30
31                # connect child list to original next
32                temp.next = next_node
33
34                if next_node:
35                    next_node.prev = temp
36
37            curr = curr.next
38
39        return head