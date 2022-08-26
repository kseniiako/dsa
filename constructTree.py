from collections import deque
from arrayBasedTree import treeToArray

# Given two integer arrays representing the preorder and inorder
# traversals of a binary tree, construct and return the binary tree.

# I love this problem so much! The three solutions below are
# all variations on the same ideas, a result of tinkering with
# my initial/naive implementation and trying to incrementally 
# optimize it.

# Technically this function just needs to return the head of the tree,
# but I am returning the tree represented as a complete binary tree array,
# as defined in the module arrayBasedTree that I wrote. (Available here: 
# https://github.com/brasssmonkey/dsa/blob/main/arrayBasedTree.py).
# This helps a lot in testing as it's easy to visualize your results.
# Note that runtime/space use of treeToArray is not accounted for in 
# the asymptotic analysis.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # My first take on this problem. All three solutions hinge on
        # a recursively called function buildHelper that puts 
        # together the tree in a dfs fashion.

        # Putting the nodes in the same sequence as they
        # are given in preorder into a stack.
        stack = deque(preorder)
        head = TreeNode(stack.popleft())

        # Helper function will recursively give us only relevant
        # portions of the inorder array to look for left/right-side
        # children of a parent at a given level
        def buildHelper(stack, inorder, head):
            if not stack:
                return
            i = 0

            # setting i to be the index of the head node at the current
            # level of traversal
            while inorder[i] != head.val:
                i += 1
            
            # if current head is not the first element in the current
            # slice of the inorder array, it means it has a left-side child.
            # append it.
            if i != 0:
                head.left = TreeNode(stack.popleft())
                # call buildHelper on the tree portion on the left of
                # the current head
                buildHelper(stack, inorder[:i], head.left)

            # if current node is not the last element in the current
            # slice of the inorder array, it means it has a right-side child.
            # append it.
            if i != len(inorder)-1:
                head.right = TreeNode(stack.popleft())
                # call buildHelper on the tree portion on the right of
                # the current head
                buildHelper(stack, inorder[i+1:], head.right)
        
        # call buildhelper on the whole inorder array.
        buildHelper(stack, inorder, head)
        
        return treeToArray(head)

        # O(n) time to build a stack. O(n) calls to buildHelper. Together, 
        # calls to buildHelper run in O(n^2) time since each call entails
        # an iteration through progressively smaller slices of an n-sized inorder array. 
        # (In the worst case scenario, next slice is only one element shorter
        # than the previous one, and time complexity for completing all recursive calls
        # is O(n^2). In the best case scenario, the slice is constantly
        # halved and the time complexity for all recursive calls becomes O(nlogn).) 
        # Therefore, total time complexity is O(n + n^2) -> O(n^2).

        # O(n) space for preorder stack.
        # Function call stack is as big as tree height, which makes it use O(logn) 
        # space in the average case and O(n) space in the worst case. However,
        # given the sizes of the arguments passed to buildHelper (we pass slices of 
        # n-sized inorder array to buildHelper, see more on that above), space use of each
        # call is O(n). Hence all the recursive calls taken together need O(n^2) space.
        # Total space complexity is therefore O(n^2)+O(n) -> O(n^2).

        # Having to iterate through array slices in every call to buildHelper is a big 
        # slowdown. It is also a pain to save array slices in memory. The solution below 
        # improves on these problems by putting the elements in inorder array into a 
        # hashmap. We also keep track of current slices in inorder array by updating 
        # indices [start, finish] instead of passing the whole slice to a function as a 
        # new object.
        
    def buildTree1(self, preorder, inorder):
        
        stack = deque(preorder)
        head = TreeNode(stack.popleft())

        # populate inorder dictionary.
        inorder_dct = {}
        for i in range(len(inorder)):
            inorder_dct[inorder[i]] = i

        def buildHelper(head, start, finish):

            i = inorder_dct[head.val]

            if i != start:
                head.left = TreeNode(stack.popleft())
                if start < i-1:
                    buildHelper(head.left, start, i-1)
            if i != finish:
                head.right = TreeNode(stack.popleft())
                if i+1 < finish:
                    buildHelper(head.right, i+1, finish)
        
        buildHelper(head, 0, len(inorder)-1)

        return treeToArray(head)

        # O(n) time. (Each of n calls to buildHelper runs in constant time -> total is
        # O(n) time; creating a dictionary and stack is also O(n) time for each.)
        # O(n) worst-case, O(logn) average-case space complexity of the function call
        # stack (equal to tree height). O(n) space for the hashmap/dictionary and O(n)
        # space for the stack.

        # Total: O(n) time, O(n) space.

    # Below is an improvement on the previous function: we get rid of the costs of
    # transforming the preorder array into a stack by storing an index to iterate over
    # the preorder array instead.

    def buildTree2(self, preorder, inorder):
        
        # head is the first node in preorder
        head = TreeNode(preorder[0])

        # populate the dictionary storing the position of
        # each element in inorder array.
        inorder_dct = {}
        for i in range(len(inorder)):
            inorder_dct[inorder[i]] = i

        # current position in preorder: state must be preserved
        # over all iterations of buildHelper.
        preorder_ind = 1

        def buildHelper(head, start, finish):

            nonlocal preorder_ind

            i = inorder_dct[head.val]

            if i != start:
                head.left = TreeNode(preorder[preorder_ind])
                preorder_ind += 1
                
                if start < i-1:
                    buildHelper(head.left, start, i-1)

            if i != finish:
                head.right = TreeNode(preorder[preorder_ind])
                preorder_ind += 1
            
                if i+1 < finish:
                    buildHelper(head.right, i+1, finish)

        buildHelper(head, 0, len(inorder)-1)

        return treeToArray(head)

        # O(n) time, O(n) space (same asymptotic complexity as previous function).

if __name__ == "__main__":
    my = Solution()
    print(my.buildTree([3,9,20,15,7], [9,3,15,20,7]))
    print(my.buildTree1([3,9,20,15,7], [9,3,15,20,7]))
    print(my.buildTree1([3,1,2,4], [1,2,3,4]))

    print(my.buildTree2([3,9,20,15,7], [9,3,15,20,7]))
    print(my.buildTree2([3,1,2,4], [1,2,3,4]))

    print([9,3,15,20,7][:0])


            


            
                

            