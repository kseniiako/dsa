# given the root of a binary tree, return its maximum
# depth. 

# a binary tree's maximum depth is the number of nodes
# along the longest path from the root node down the 
# farthest leaf node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution():
    def maxDepth(self, root):
        def MaxDepthHelper(root, count):
            if root:
                count +=1
                return max(MaxDepthHelper(root.left, count), MaxDepthHelper(root.right, count))
            else:
                return count
    
    def maxDepthIter(self, root):
        stack = collections.deque([])

        depth = 0

        if root:
            depth += 1
            stack.append((root, depth))

    
        while stack:

            current_node, current_depth = stack.popleft()


            if current_node.left:
                stack.append((current_node.left, current_depth + 1))
            if current_node.right:
                stack.append((current_node.right, current_depth + 1))
            
            
            depth = max(depth, current_depth)
        
        return depth

TN5 = TreeNode(5)
TN4 = TreeNode(4)
TN3 = TreeNode(3)
TN2 = TreeNode(2, TN4, TN5)
TN1 = TreeNode(1, TN2, TN3)

my = Solution()
#import pdb; pdb.set_trace()
print(my.maxDepthIter(TN1))



