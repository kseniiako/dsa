# Validate Binary Search Tree (Leetcode 98)

# Given the root of a binary tree, determine if it is a valid BST.

# That is:
# 1. The left subtree of a node contains only nodes with keys less
# than the node's key.
# 2. The right subtree of a node contains only nodes with keys greater
# than the node's key.
# 3. Both the left and right subtrees must also be BSTs.


from collections import deque
from math import inf

from arrayBasedTree import arrayToTree

class Solution:
    def isValidBST(self, root):
        # We'll traverse the tree depth-first (iteratively, using
        # a stack). Alternatively, we could have a queue and perform
        # breadth-first traversal.
        stack = deque([(root, -inf, inf)])

        while stack:
            cur, low_bound, high_bound = stack.pop()
            
            if cur.val <= low_bound or cur.val >= high_bound:
                return False 

            if cur.left:
                stack.append((cur.left, low_bound, cur.val))
            
            if cur.right:
                stack.append((cur.right, cur.val, high_bound))
        
        return True

    # O(n) time (we visit each node exactly once).
    # O(n) space. The DFS stack will keep at most
    # O(tree_height) nodes. This is up to n nodes
    # (the whole tree) in the worst case scenario, although
    # for a complete tree its height would only amount to
    # O(logn) nodes.

    # Some commenters on Leetcode said that DFS with a stack
    # is faster than BFS with a queue in this problem. While time
    # complexity is O(n) in both cases, I guess this might be true
    # since we _might_ operate with a smaller set of different values
    # (for low and high bounds) in the DFS case, and the compiler
    # may therefore provide some optimizations. However, this is just
    # a guess, and I currently lack knowledge to affirm that DFS would
    # be faster. Let's consider them equal for now.

if __name__ == "__main__":
    my = Solution()
    tree1 = arrayToTree([2,1,3])
    print(my.isValidBST(tree1))

    tree2 = arrayToTree([5,1,4,None,None,3,6])
    print(my.isValidBST(tree2))