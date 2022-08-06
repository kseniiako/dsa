# balanced Binary Tree (leetcode 110)

# given a binary tree, determine if it's height-balanced

# a binary tree in which the left and the right subtrees of
# every node differ in height by no more than one

# a brute-force solution could be to find
# the heights of the two brances and compare them.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def isBalanced(self, root):
        # this solution is the approach 1 (top-down recursion)
        # from leetcode.
        def height(node):
            if not node:
                return -1
            
            return 1+max(height(node.left), height(node.right))
        
        if not root:
            return True

        if abs(height(root.left) - height(root.right)) > 1:
            return False
        
        return ( self.isBalanced(root.left) & self.isBalanced(root.right) )

    
    def isBalancedBottomUp(self, root):
        # this is an erroneous attempt at implementing Approach 2
        # from leetcode. Why is it erroneous? It preserves the
        # redundancy present in Appr1: we re-count the height of a subtree
        # once for each parent of the subtree.


        def height(node):
            if not node:
                return -1
            return 1+max(height(node.right), height(node.left))

        left = self.isBalancedBottomUp(root.left)
        right = self.isBalancedBottomUp(root.right)

        if left and right:
            return abs(height(root.left) - height(root.right)) < 1
        else:
            return False

    def BalancedBottomUpCorrect(self, root):
        # LC Approach 2. Make the helper function return
        # a tuple so that we keep track of tree height
        # along with balance. 
        def isBalanceHelper(node):
        # emptry tree: balanced, let's set height to be -1
        # (analogous thinking to our height implementation)
            if not node:
                return (True, -1)
            
            balance_left, height_left = isBalanceHelper(node.left)
            if not balance_left:
                return (False, 0) # we don't account for height in this
                                # return value since we already know that
                                # tree is not balanced

            balance_right, height_right = isBalanceHelper(node.right)
            if not balance_right:
                return (False, 0)
            
            # Now, if the two substrees are balanced, check current 
            # tree balance. The height values are already available.
            return ( (abs(height_left - height_right) < 2), 
            1 + max(height_left, height_right) )

        return isBalanceHelper(root)[0]

    def elegantIsBalanced(self, root):
        # this solution can do without tuples
        # because it uses output -1 for invalid returns
        # (i. e. to show that tree is unbalanced).
        # On the contrary, for a null node a 0 is returned. 
        # The function immediately returns upon finding an
        # imbalanced subtree. (This is my small improvement
        # to this algorithm as found in Leetcode comments:
        # I don't wait for both subtrees to be checked
        # if the first subtree returns -1.) 
        def check_height(node):
            if not node:
                return 0

            left = check_height(node.left)
            if left == -1:
                return left

            right = check_height(node.right)
            if right == -1:
                return right

            if abs(left - right) > 1:
                return -1 

            return 1 + max(left, right)
        
        return check_height(root) != -1 

            


            


            
        
        
