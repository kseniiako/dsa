import sys
from collections import deque

# Tree node
class Node:
        def __init__(self, value = None, parent = None, child1 = None, child2 = None):
            self.value = value
            self.parent = parent
            self.child1 = child1
            self.child2 = child2

class ValidateTree:
    def __init__(self):
        
        # this is the set where we will store all the edges we come upon (to check for duplicates
        # and then pass to the function addNode that will create the node objects)
        self.edgeSet = set()

        # store visited/seen nodes in a dictionary where {key : value} is {node value : Node object}
        self.seen_nodes = {}

        # store root nodes (no parent) in a set.
        # when the tree is wholly constructed, no parentless nodes is one of the possible
        # indications of E5 (cycle). More than one root/parentless node is E4.
        self.parentless_nodes = set()
    
        self.output = ""
        
    # Function to add a new edge to the set of edges
    def addEdge(self, st):
        if st[1] != "," or not ("A" <= st[0] <= "Z") \
        or not ("A" <= st[2] <= "Z"):
            print("E1")
            return 1

        par, ch = st[0], st[2]
        
        # if this edge is already present, we have E2.
        if (par, ch) in self.edgeSet:
            return 1
        self.edgeSet.add((par, ch))

    # Function to add nodes to a tree by creating node objects. A parent and child
    # values are passed to it.
    def addNodes(self, par, ch):           
        # add nodes is they don't exist
        if par not in self.seen_nodes:
            self.seen_nodes[par] = Node(par)
            # if this parent has never been seen before, it is definitely
            # parentless (a root)
            self.parentless_nodes.add(self.seen_nodes[par])

        par_node = self.seen_nodes[par]

        if ch not in self.seen_nodes:
            self.seen_nodes[ch] = Node(ch)
        ch_node = self.seen_nodes[ch]
            
        # set parent and delete current child from parentless_nodes set
        # (if child is present there)
        ch_node.parent = par_node
        self.parentless_nodes.discard(ch_node)
            
        # set children of parent in the correct lexicographic order
        if not par_node.child1:
            par_node.child1 = ch_node
        elif not par_node.child2:
            if ch_node.value >= par_node.child1.value:
                par_node.child2 = ch_node
            else:
                par_node.child2 = par_node.child1
                par_node.child1 = ch_node
        # if parent already has two children and we try to add one more,
        # return E3 (a parent has more than 2 children)
        else:
            print("E3")
            return 1
            
    # Function to print out the tree in the correct format
    def printTree(self, node):
            
        # uses a LIFO stack to keep track of nodes and parentheses
        stack = deque([")", node])
            
        # Use a set to keep track of nodes already added to output:
        # this is a way to efficiently check for cycles. We perform
        # the cycle check while putting together the output, without having to run an extra 
        # iteration over all tree nodes before computing the output to check for cycles.
        added_nodes = set()

        while stack:
            cur = stack.pop()

            if cur == ")":
                self.output+=")"
                    
            elif cur in added_nodes:
                print("E5")
                return 1

            else:
                added_nodes.add(cur)
                self.output += "("
                self.output+=cur.value 
                if cur.child2:
                    stack.append(")")
                    stack.append(cur.child2)
                if cur.child1:
                    stack.append(")")
                    stack.append(cur.child1)

        print(self.output)

    # Validator function that reads in the input string and prints out
    # tree or first relevant error in [E1, E2, E3, E4, E5].
    def validate(self):

        # reading in the input and checking that it's just one line
        input_line = sys.stdin.readlines()
        if len(input_line) > 1:
            print("E1")
            return
        
        input_line = input_line[0]

        i = 0
        max_ind = len(input_line)
        
        duplicate_set = False
        
        if input_line[i] != "(" or input_line[max_ind-1] != ")":
            print("E1")
            return
        
        # iterate through the input string, check for validity,
        # and add edges.
        while i <= max_ind - 4 and input_line[i] == "(":
            if self.addEdge(input_line[i+1:i+4]):
                duplicate_set = True
            i += 4

            if input_line[i] != ")":
                print("E1")
                return

            if i == max_ind - 1:
                break
            else:
                if i+2 >= max_ind or input_line[i+1] != " " or input_line[i+2] != "(":
                    print("E1")
                    return
            i += 2
                    
        # if we haven't gotten to the end of the string index, the input format is wrong
        if i != max_ind - 1:
            print("E1")
            return
        
        # check for duplicate edges
        if duplicate_set:
            print("E2")
            return
        
        # iterate over all edges to add all the nodes to the tree
        for par, ch in self.edgeSet:
            if self.addNodes(par, ch):
                return 
        
        # check if there is more than one root
        if len(self.parentless_nodes) > 1:
            print("E4")
            return
        
        # check if there are no roots
        if not self.parentless_nodes:
                print("E5")
                return 1
            
        # get root for printing out the tree
        root = [x for x in self.parentless_nodes][0]

        self.printTree(root)

        return

#Driver code
def main():
    my = ValidateTree()
    my.validate()
    
main()