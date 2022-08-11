# Leetcode 199: Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing
# on the right side of it and return the values of nodes you
# can see ordered from top to bottom.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # The following are three solutions, all of them
    # rely on BFS (implemented with a queue). We're using
    # the variable that holds the current node to append
    # the current node to the output array in the case that
    # current node is the last one on its level.

    # The differences between the three approaches boil
    # down to the way they signal switch from one level
    # (row of nodes) to the next.

    def rightSideView(self, root):
        # This approach uses two separate
        # queues for current and next level/row.
        out = []

        # handle trivial case: tree is empty
        if not root:
            return out

        out = []
        current_level = deque([root])
        next_level = deque([])

        while len(current_level) != 0:
            
            cur_node = current_level.popleft()

            if cur_node.left:
                next_level.append(cur_node.left)
                
            if cur_node.right:
                next_level.append(cur_node.right)

            # if we're at the end of current level,
            # update output array and set current level 
            # to the next one, next level to empty.
            if len(current_level) == 0:
                out.append(cur_node.val)

                current_level = next_level
                next_level = deque([])

        return out

    def rightSideView1(self, root):
        # This approach uses sentinel nodes
        # with None values to signal end of level/row.

        out = []
        if not root:
            return out
        
        sentinel = TreeNode(None)

        # put sentinel at the end of current level
        tree_view = deque([root, sentinel])

        # set first current node to sentinel value:
        # before root, we have nothing.
        cur_node = sentinel

        while len(tree_view) > 0:
            
            prev_node, cur_node = cur_node, tree_view.popleft()

            # iterate until we reach the nearest sentinel
            while cur_node.val != None:
                if cur_node.left:
                    tree_view.append(cur_node.left)
                if cur_node.right:
                    tree_view.append(cur_node.right)

                prev_node, cur_node = cur_node, tree_view.popleft()

            # once sentinel is reached, apend last node in row 
            # to output
            out.append(prev_node.val)

            # if next level is nonempty, add sentinel
            if len(tree_view) != 0:
                tree_view.append(sentinel)

        return out
    
    def rightSideView2(self, root):
        # This solution counts the number of
        # nodes on each level/row
        # to distinquish between levels.

        out = []
        if not root:
            return out
        
        tree_view = deque([root])

        while len(tree_view) != 0:
            
            # keep track of the size of current level
            level_size = len(tree_view)

            # fetch kids of all nodes in current level
            # and append them to the queue
            for x in range(0, level_size):

                cur_node = tree_view.popleft()
                
                # check if current node is the rightmost 
                # on its level
                if x == level_size - 1:
                    out.append(cur_node.val)
                    
                if cur_node.left:
                    tree_view.append(cur_node.left)

                if cur_node.right:
                    tree_view.append(cur_node.right)
        
        return out

  
if __name__ == "__main__":           
    my = Solution()

    Node5 = TreeNode(4)
    Node4 = TreeNode(5)
    Node3 = TreeNode(3, None, Node5)
    Node2 = TreeNode(2, None, Node4)
    Node1 = TreeNode(1, Node2, Node3)

    Node13 = TreeNode(3)
    Node11 = TreeNode(1, None, Node3)

    Node21 = TreeNode(8)

    print(my.rightSideView(Node1))
    print(my.rightSideView(Node11))
    print(my.rightSideView(Node21))

    print(my.rightSideView1(Node1))
    print(my.rightSideView1(Node11))
    print(my.rightSideView1(Node21))

    print(my.rightSideView2(Node1))
    print(my.rightSideView2(Node11))
    print(my.rightSideView2(Node21))

# Takeaway: remember what the cur_node varible is initialized to!
# It might be very useful.

# Takeaway: think creatively about balancing two requirements 
# during iteration: satisfying the condition of iteration and
# handling edge cases/initial input. E. g. in the second solution
# variant, current node is initialized to sentinel before the loop starts
# so that we have some value in cur_node to conveniently transfer 
# to prev_node. Root + sentinel are added to queue (queue must be 
# nonempty for iteration), and then previous node is set to 
# current node (sentinel) and current node — to the root, 
# popped out of the queue. That way we seamlessly start the cycle.
