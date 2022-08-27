# Kth Smallest Element in a Binary Search Tree (Leetcode 230)

# Given the root of a binary search tree and an integer k, return
# kth smallest value (1-indexed) of all the values of the nodes in the tree.

from collections import deque

# I wanted to use my arrayBasedTree module for testing, but unfortunately
# this problem was where my module proved insufficient/faulty. (I have to
# and I am excited to update and patch it soon!) Basically, because my
# arrayToTree function is designed to represent complete binary trees,
# it stores nodes with value None instead of nothing in the place of non-
# existent nodes in an incomplete tree. However, this should be a straightforward
# fix. Meanwhile, I used the Leetcode environment for testing.
# from arrayBasedTree import arrayToTree

# I love this function so much. It performs iterative depth-first search
# on a tree (using a stack) to find the leftest node (the first node with 
# no left children as you keep constantly going to the left) and keep that
# node's parents on the stack. As we start our count at position 1 (first
# smallest node), we go through the parent nodes, and if any of them have 
# right children, we go to the right child and then as far leftwards as possible 
# to reach the second smallest node. This process is repeated iteratively!

# The type of tree traversal (left->parent->right) that comes in so handy for
# finding kth smallest node in a binary search tree is called inorder traversal.

class Solution:
    def kthSmallest(self, root, k):
        stack = deque([])
        start = root
        stack.append(start)

        while start.left:
            start = start.left
            stack.append(start)
        
        count = 1
        cur = stack.pop()

        while count < k:

            if cur.right:
                cur = cur.right
                stack.append(cur)
                while cur.left:
                    cur = cur.left
                    stack.append(cur)
 
            cur = stack.pop()
            count += 1

        return cur.val
    
# O(h+k) time, O(h) space, where h is tree height.

# Breakdown:
# O(tree_height+k) time (possibly going through all levels of the tree 
# as we descend leftwards, and then going back up/to the right and
# down again in order to get the kth smallest node). For a balanced
# tree, this translates to O(log n + k), and for a tree that has all its
# nodes in the left subtree (worst-case scenario), this is O(n+k) time
# complexity.
# O(h) space (for the stack). Note that the stack can only be as big
# as tree height, which is O(logn) in the average case, and O(n) in
# the worst case!


