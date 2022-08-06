# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
    
    def invertTreeIter(self, root):

        q = collections.deque([])

        if root:
            q.append(root)
        else:
            return root
        
        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            
            if cur.right:
                q.append(cur.right)
 
            cur.left, cur.right = cur.right, cur.left

        return root

