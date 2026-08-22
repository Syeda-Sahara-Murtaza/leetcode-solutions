1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head):
9        slow = head
10        fast = head
11
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15
16            if slow == fast:
17                slow = head
18
19                while slow != fast:
20                    slow = slow.next
21                    fast = fast.next
22
23                return slow
24
25        return None