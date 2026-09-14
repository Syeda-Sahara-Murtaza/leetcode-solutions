1# from collections import deque
2# class Solution:
3#     def firstUniqChar(self, s: str) -> int:
4#         queue=deque()
5#         count={}
6#         for i,character in enumerate(s):
7#             count[character]=count.get(character,0) + 1
8#             queue.append((character,i))
9#             while queue and count[queue[0][0]] > 1:
10#                 queue.popleft()
11#         return queue[0][1] if queue else -1
12
13from collections import deque
14class Solution:
15    def firstUniqChar(self, s: str) -> int:
16        queue = deque()
17        counts = {}
18        for i, character in enumerate(s):
19            counts[character] = counts.get(character, 0) + 1
20            queue.append((character, i))
21            while queue and counts[queue[0][0]] > 1:
22                queue.popleft()
23        return queue[0][1] if queue else -1
24