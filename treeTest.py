#def testInput(str)

import sys
from collections import deque

class Node:
    def __init__(self, value = None, parent = None, child1 = None, child2 = None):
        self.value = value
        self.parent = parent
        self.child1 = child1
        self.child2 = child2

def main():

    seen_nodes = {}
    parentless_nodes = set()

    def addNodes(st):
        if st[1] != "," or not ("A" <= st[0] <= "Z") \
        or not ("A" <= st[2] <= "Z"):
            print("E1")
            return 1

        par, ch = st[0], st[2]

        if par in seen_nodes and ch in seen_nodes:
            if (seen_nodes[par].child1 and \
                (seen_nodes[par].child1.value == ch) ) or \
                (seen_nodes[par].child2 and \
                (seen_nodes[par].child2.value == ch)):
                print("E2")
                return 1
        if par == ch:
            print("E5")
            return 1
        
        
        if par not in seen_nodes:
            seen_nodes[par] = Node(par)
            parentless_nodes.add(seen_nodes[par])

        par_node = seen_nodes[par]

        if ch not in seen_nodes:
            seen_nodes[ch] = Node(ch)
        ch_node = seen_nodes[ch]

        # does the "multiple roots" error mean multiple parents of any
        # node? I am interpreting "multiple roots" conservatively, to only
        # mean that the tree as a whole has more than 1 root (more than
        # 1 node without a parent). I assume a lot of the cases of one node
        # having multiple parents would be caught when we check that the node
        # has no cycles.
        if ch_node.parent == par_node:
            print("E2")
            return 1

        ch_node.parent = par_node
        parentless_nodes.discard(ch_node)

        if not par_node.child1:
            par_node.child1 = ch_node
        elif not par_node.child2:
            if ch_node.value >= par_node.child1.value:
                par_node.child2 = ch_node
            else:
                par_node.child2 = par_node.child1
                par_node.child1 = ch_node

        else:
            print("E3")
            return 1
    
    def printTree(node, output):
        deq = deque([")", node])

        added_nodes = set()

        while deq:
            cur = deq.pop()

            if cur == ")":
                output+=")"

            elif cur in added_nodes:
                print("E5")
                return 1

            else:
                added_nodes.add(cur)
                output += "("
                output+=cur.value 
                if cur.child2:
                    deq.append(")")
                    deq.append(cur.child2)
                if cur.child1:
                    deq.append(")")
                    deq.append(cur.child1)

        print(output)

    input_line = sys.stdin.readlines()
    if len(input_line) > 1:
        print("E1")
        return
    
    input_line = input_line[0]

    i = 0
    max_ind = len(input_line) - 1

    while i < max_ind-4 and input_line[i] == "(":
        if addNodes(input_line[i+1:i+4]):
            
            return
        else:
            i += 4

        if input_line[i] != ")":
            print("E1")
            return

        if i == max_ind:
            return
        else:
            i += 2

    if i != len(input_line):
        print("E1")
        return
    
    if len(parentless_nodes) > 1:
        print("E4")
        return

    if not parentless_nodes:
            print("E5")
            return 1
        
    root = [x for x in parentless_nodes][0]

    printTree(root, "")

    return

if __name__ == "__main__":
    main()


