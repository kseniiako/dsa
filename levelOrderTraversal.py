# Given the root of a binary tree, return the 
# level order traversal of its nodes' values
# (i. e. from left to right, level by level). 
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        # this solution will employ BFS
        q = deque([root])
        out = []

        while q:

            # keep track of size of current level
            level_size = len(q)

            # to the output list of lists,
            # add empty list to represent current level.
            out.append([])

            for x in range(level_size):

                cur_node = q.popleft()

                if cur_node:
                    out[-1].append(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)
        
        if not out[-1]:
            out = out[:-1]

        return out

if __name__ == "__main__":

    my = Solution()
    Node5 = TreeNode(5)
    Node4 = TreeNode(4)
    Node3 = TreeNode(3, None, Node5)
    Node2 = TreeNode(2, None, Node4)
    Node1 = TreeNode(1, Node2, Node3)

    print(my.levelOrder(Node1))


            