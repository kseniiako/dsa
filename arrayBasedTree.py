# Functions that convert binary tree into array representation
# and, vice versa, use an input array to represent a binary tree.

# Rules for array-based representation of a binary tree:
# If p is the root, then f(p) = 0 (i. e. position of p in 
# array is 0). 
# If p is the left child of q, then f(p) = 2f(q) + 1.
# If p is the right child of q, then f(p) = 2f(q) + 2.

from collections import deque

class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def treeToArray(root):
    # return representation of a binary tree
    # via an array

    out = []
    if not root:
        return out
    
    out.append(root.val)
    queue = deque([root])

    lvl_size = 1
    nones_count = 0

    while lvl_size != nones_count:

        nones_count = 0
        lvl_size *= 2

        for _ in range(len(queue)):

            cur_node = queue.popleft()

            if cur_node.left:
                out.append(cur_node.left.val)
                queue.append(cur_node.left)
            else:
                out.append(None)
                queue.append(TreeNode(None))
                nones_count += 1

            if cur_node.right:
                out.append(cur_node.right.val)
                queue.append(cur_node.right)
            else:
                out.append(None)
                queue.append(TreeNode(None))
                nones_count+=1

    # now we're going to trim the tree and remove trailing
    # none nodes (it is obvious that nodes not present in the
    # tree at the last level are nonexistent)
    out = out[:-lvl_size]

    i = len(out)- 1
    while not out[i] and i > -1:
        i -= 1
    return out[:i+1]


def arrayToTree(arr):
    # given an array representing a complete binary tree
    # (such as an output of treeToArray), return the tree in
    # standard form

    # handling empty array input
    if not arr:
        return None

    root = TreeNode(arr[0])

    # we will use a queue to hold tuples of
    # (node, position in array)
    queue = deque([(root, 0)])
    pos_right = 0

    while queue and (pos_right < (len(arr) - 1)):
        
        cur_node, cur_pos = queue.popleft()

        #find positions of the node's childern
        pos_left = (2*cur_pos)+1
        pos_right = pos_left + 1

        if pos_left < len(arr) and arr[pos_left]:
            cur_node.left = TreeNode(arr[pos_left])
            queue.append((cur_node.left, pos_left))
        
        if pos_right < len(arr) and arr[pos_right]:
            cur_node.right = TreeNode(arr[pos_right])
            queue.append((cur_node.right, pos_right))
    
    return root
        
        
    

if __name__ == "__main__":

    Node6 = TreeNode(5)
    Node5 = TreeNode(1)
    Node4 = TreeNode(3)
    Node3 = TreeNode(4, Node5, Node6)
    Node2 = TreeNode(1, Node4)
    Node1 = TreeNode(3, Node2, Node3)

    array1 = [3, 1, 4, 3, None, 1, 5]

    print(treeToArray(Node1))

    # testing how the functions work together
    test1 = arrayToTree(array1)
    print(test1.val)
    print(treeToArray(test1))

    array2 = [3,1,4,None,2]
    test2 = arrayToTree(array2)
    print(test2.val)
    print(test2.left.val)
    print(treeToArray(test2))

    # The following line returns an AttributeError
    # since we're trying to get the value of a nonexistent
    # node (is is a None value in the list).
    # print(arrayToTree(array2).left.left.val)

    test3 = arrayToTree([5,3,6,2,4,None,None,1])
    print(test3.val)
    print(test3.right.val)
    print(treeToArray(test3))
        
            

