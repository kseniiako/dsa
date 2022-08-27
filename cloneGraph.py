# Clone Graph (Leetcode 133)

# Given a reference of a node in a connected undirected graph,
# return a deep copy (clone) of the graph.

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None)
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

# Working solution: yet to be made cleaner and more succinct!

class Solution:
    def cloneGraph(self, node):
        # We will use a queue to store nodes to facilitate
        # breadth-first search. Depth-first search with a stack 
        # would be an equally viable option.
        if not node:
            return None
        # store visited nodes in a set
        visited = {}

        # this variable will store a reference to the
        # start node in the cloned array
        new_node = Node()
        q = deque([(node, new_node)])

        while q:
            cur, new_cur = q.popleft()
            
            new_cur.val = cur.val
            if cur not in visited:
                visited[cur] = new_cur
                
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    new_neighbor = Node()
                    new_neighbor.neighbors.append(new_cur)
                    new_cur.neighbors.append(new_neighbor)

                    q.append((neighbor, new_neighbor))
                    visited[neighbor] = new_neighbor
                else:
                    if visited[neighbor] not in new_cur.neighbors:
                        new_cur.neighbors.append(visited[neighbor])
                    
        return new_node

