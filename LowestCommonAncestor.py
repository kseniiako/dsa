# Given a binary search tree, find the lowest common ancestor
# (LCA) node of two given nodes in the BST. 

# The lowest common ancestor is defined between two nodes
# p and q as the lowest node in T that has both p and q
# as descendants (we allow a node to be a descendant of itself).

class Solution:
    def LCA(self, root, p, q):
        if p.val > q.val:
            greater, smaller = p, q
        else:
            smaller, greater = p, q
        
        cur_node = root

        while cur_node:
            if ( (cur_node.val >= smaller.val) & 
            (cur_node.val <= greater.val) ):
                return cur_node
        
            if cur_node.val > greater.val:
                cur_node = cur_node.left
        
            else:
                cur_node = cur_node.right
        


        

