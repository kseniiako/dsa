# Given a binary tree, a node in it is named "good"
# if on the path from root to X there are no nodes
# with value greater than x. 
# Return number of good nodes in a binary tree. 

# Leetcode 1448

from collections import deque

class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root):
        # This solution traverses the tree depth-first.

        if not root:
            return 0
        
        # root is always a good node, so we initially
        # set the count of good nodes to 1.
        good_count = 1

        # we will conduct a depth-first search and use a stack
        # to hold tuples of (node, max value in the tree preceding
        # or at the node)

        # initally the max value is that of root
        stack = deque([(root, root.val)])

        while stack:
            cur_node, cur_max = stack.pop()
            
            if cur_node.left:
                if cur_node.left.val >= cur_max:
                    good_count += 1
                stack.append((cur_node.left, max(cur_node.left.val, cur_max)))
            
            if cur_node.right:
                if cur_node.right.val >= cur_max:
                    good_count += 1
                stack.append((cur_node.right, max(cur_node.right.val, cur_max)))

        return good_count
            
if __name__ == "__main__":

    Node6 = TreeNode(5)
    Node5 = TreeNode(1)
    Node4 = TreeNode(3)
    Node3 = TreeNode(4, Node5, Node6)
    Node2 = TreeNode(1, Node4)
    Node1 = TreeNode(3, Node2, Node3)

    my = Solution()
    print(my.goodNodes(Node1))







