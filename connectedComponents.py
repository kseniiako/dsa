# Number of Connected Components in an Undirected Graph (Leetcode 323)

# You have a graph of n nodes. You are given an integer n and an array
# edges where edges[i] = [a, b] indicates that there is an edge between
# a and b in the graph.

# Return the number of connected components in the graph.

# 1. (DFS Approach from the Leetcode article). This approach is implemented in function
# countComponentsDFS.
# Let's see how we can use DFS to solve the problem. If we run DFS, starting
# from a particular vertex, it will continue to visit the vertices depth-wise until
# there are no more adjacent vertices left to visit. Thus, it will visit all of the vertices
# within the connected component that contains the starting vertex. Each time we
# finish exploring a connected component, we can find another vertex that has not been
# visited yet, and start a new DFS from there. The number of times we start a new DFS
# will be the number of connected components.

# Complexity analysis. E is the number of edges, V — number of vertices.
# Time complexity: O(E + V). Building the adjacency list will take O(E)
# operations, as we iterate over the list of edges once and insert each edge
# into two lists. During the DFS traversal, each vertex will only be visited once.
# This is because we mark each vertex as visited as soon as we see it, and then
# we only visit vertices that are not marked as visited. In addition, when we
# iterate over the edge list of the vertex, we look at each edge once. This
# has a total cost of O(E + V).
# Space complexity: O(E + V).
# The adjacency list will take O(E) space. To keep track of visited
# vertices, an array of size O(V) is required. Also, the runtime stack for DFS
# will use O(V) space.

from collections import deque

class Solution:
    def countComponents(self, n, edges):
        # My initial attempt at solving this.
        # A working yet very slow solution. Need to study and
        # try union find instead!
        connected = []

        all_elements = set()
        count_groups = 0
        
        for node1, node2 in edges:
            all_elements.add(node1)
            all_elements.add(node2)
            
            cur_group = -1
            for i in range(len(connected)):
                if cur_group == -1:
                    if node1 in connected[i]:
                        connected[i].add(node2)
                        cur_group = i
                    elif node2 in connected[i]:
                        connected[i].add(node1)
                        cur_group = i
                elif node1 in connected[i] or \
                node2 in connected[i]:
                    connected[cur_group] |= connected[i]
                    connected[i] = []
                    count_groups -= 1
                    
                if len(connected[cur_group]) == n:
                    return 1
                
            if cur_group == -1:
                connected.append({node1, node2})
                count_groups+=1

        if len(all_elements) < n:
            return(count_groups + (n - len(all_elements)))
        return count_groups

    def countComponentsDFS(self, n, edges):
        # DFS solution — ad explained in the Leetcode article and comment
        # section (by user shreshtavinayak).

        # This solution heavily exploits the fact that the node values
        # are necessarily in range(n) for an n-sized graph. 

        # Adjacency list. At each index n, it holds all nodes adjacent to 
        # node with value n.
        adj = [[] for x in range(n)]
        # Set to keep track of visited nodes.
        visited = set()
        # Counter of distinct connected components.
        counter = 0
        
        # Function to perform DFS
        def dfs(v):
            for node in adj[v]:
                if node not in visited:
                    visited.add(node)
                    dfs(node)

        # First, we populate the adjacency list.
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # Then, for every node, if we have not visited it yet,
        # this means this node is our "entry point" to a new connected
        # component. We add this node to the visited set, increment counter 
        # by 1, and run dfs on this node to visit all the nodes in this 
        # connected component.
        for i in range(n):
            if i not in visited:
                visited.add(i)
                counter += 1
                dfs(i)

        # return counter
        return counter

    def countComponentsIterativeBFS(self, n, edges):
        # This solution is very similar to the previous one, but it
        # uses BFS with a queue instead of a recursive dfs. This may
        # significantly improve memory use since we end up having an
        # O(1) call stack instead of an O(n) call stack.
        adj = [[] for x in range(n)]
        visited = set()
        counter = 0
        
        # Function to perform BFS
        def bfs(v):
            q = deque([v])
            
            while q:
                cur = q.popleft()
                if cur not in visited:
                    visited.add(cur)
                    for x in adj[cur]:
                        q.append(x)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        for i in range(n):
            if i not in visited:
                counter += 1
                bfs(i)

        return counter

        # O(E + V) time complexity. O(E) operations to build the adjacency
        # list, O(V) operations during BFS (each vertex is only visited once).

        # O(E + V) space complexity. The adjacency list takes O(E) space. To keep
        # track of visited vertices, an array of size O(V) is required. The BFS
        # queue may take up O(V) space.

    def countComponentsUnionFind(self, n, edges):
        parents = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(n1):
            # find root parent of n1
            res = n1

            while res != parents[res]:
                # path compression!
                # before we go to the parent, we want to set parent
                # of result equal to its grandparent 
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res

        def union(n1, n2):
            # this function returns 0 if the two nodes are already connected
            # and 1 if they form a new connection.
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                rank[p1] > rank[p2]
                parents[p2] = p1
                rank[p1] += rank[p2]
            return 1

        # max number of connected components is n: this is the case when all nodes are
        # disconnected.
        res = n

        # check for each edge: if it creates a new connection, then the number of connected components
        # was just reduced by 1.
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res

        # Space complexity: O(V). Storing the representative/parent of each
        # vertex takes O(V) space (the parents array). Moreover, storing the
        # sizes of the components (the rank array) also takes O(V) space.

        # Time complexity: O(E * a(n)), where a(n) is the inverse Ackermann function.
        # Iterating over every edge requires O(E) operations, and for every operation,
        # we are performing the combine method, which is O(a(n)), where a(n) is the
        # inverse Ackermann function. In practice, we may assume a(n) is < 5 for any
        # practical input size n, and treat a(n) as a constant (getting time complexity
        # O(E)).

if __name__ == "__main__":
    my = Solution()
    print(my.countComponents(5, [[0,1], [1,2], [3,4]]))
    print(my.countComponents(5, [[0,1], [1,2], [2,3], [3,4]]))

    print(my.countComponentsUnionFind(5, [[0,1], [1,2], [3,4]]))
    print(my.countComponentsUnionFind(5, [[0,1], [1,2], [2,3], [3,4]]))




