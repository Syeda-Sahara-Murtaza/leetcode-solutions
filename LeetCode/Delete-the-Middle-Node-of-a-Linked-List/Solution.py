1class Solution: 
2    def deleteMiddle(self, head): 
3        if head.next is None: 
4            return None
5        slow = head 
6        fast = head 
7        prev = None 
8        while fast and fast.next: 
9            prev = slow 
10            slow = slow.next 
11            fast = fast.next.next 
12        prev.next = slow.next 
13        return head
14
15
16
17
18
19
20
21
22# prev = None is used to keep track of the node before slow, so we can connect it to slow.next and delete the middle node.
23
24
25# Definition for singly-linked list.
26# class ListNode:
27#     def __init__(self, val=0, next=None):
28#         self.val = val
29#         self.next = next