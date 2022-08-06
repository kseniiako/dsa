# Leetcode 543: find the diameter of the binary tree:
# that is, the length of the longest path between any two
# nodes in a tree.

class Solution():
    def diameterOfBinaryTree(self, root):
        max_diameter = 0
        
        def longestPath(node):
            
            nonlocal max_diameter
            
            if not node:
                return 0
            
            else:
                left = longestPath(node.left)
                right = longestPath(node.right)
                current_path = left + right
                max_diameter = max(current_path, max_diameter)

            return max(left, right) + 1
        
        longestPath(root)
        return max_diameter

# Very beautiful algorithm! I enjoyed learning this
# so much, and I now know about the keyword "nonlocal"!

