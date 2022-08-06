# given the roots of two binary trees 
# root and subroot, return True if there is
# a subtree of root with the same
# structure and node values as subroot
# and false otherwise.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subroot):

        def isSameTreeIter(p, q):
            # helper function to check if two trees
            # are the same
            # this is an iterative implementation 
            # to avoid O(n) stack usage
        
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
        
        if not subroot:
            return True

        comparisons = deque([root])

        while comparisons:
            
            cur_node = comparisons.popleft()
            
            if cur_node:
                if cur_node.val == subroot.val:
                    if ( isSameTreeIter(cur_node.left, subroot.left)
                    and isSameTreeIter(cur_node.right, subroot.right) ):
                        return True
            
                comparisons.append(cur_node.left)
                comparisons.append(cur_node.right)
        
        return False


Tr2 = TreeNode(1)
Tr1 = TreeNode(1, Tr2)

SubTr1 = TreeNode(1)

my = Solution()
print(my.isSubtree(Tr1, SubTr1))
