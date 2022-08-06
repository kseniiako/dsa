# Given the roots of two binary trees p and q, write a
# fxn to check if they are the same or not.
# (LC 100)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p, q):
        if bool(p) != bool(q):
            return False
        
        if not p:
            return True

        if p.val != q.val:
            return False
        
        return ( isSameTree(p.left, q.left) and 
        isSameTree(p.right, q.right) )

    def isSameTreeIter(self, p, q):
        # iterative solution to avoid O(n) stack
        # usage
        
        # create a queue to store pairs to compare
        comparisons = deque([(p, q)])

        while comparisons:

            node1, node2 = comparisons.popleft()

            # check if one of the nodes is null
            # while the other isn't (different trees)
            if bool(node1) != bool(node2):
                return False
            
            # if both nodes are null, condition of
            # sameness is preserved
            if node1:
                # if neither node is null, compare values
                if node1.val != node2.val:
                    return False

                # only append child node comparisons if the 
                # current nodes are not null (i. e. can
                # potentially have children)
                comparisons.append((node1.left, node2.left))
                comparisons.append((node1.right, node2.right))

        # if we haven't returned false yet, and
        # the queue is empty, we rightfully return true      
        return True
        




