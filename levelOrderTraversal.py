# Given the root of a binary tree, return the 
# level order traversal of its nodes' values
# (i. e. from left to right, level by level). 
from collections import deque

class Solution:
    def levelOrder(self, root):
        q = deque([root])
        out = []

        while q:
            out.append[[]]
            cur_node = q.pop()
            if cur_node:
                out[-1].append(cur_node.val)
                q.append(cur_node.left)
                q.append(cur_node.right)
        
        return out
            