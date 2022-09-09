# Number of Connected Components in an Undirected Graph (Leetcode 323)

class Solution:
    def countComponents(self, n, edges):
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

if __name__ == "__main__":
    my = Solution()
    print(my.countComponents(5, [[0,1], [1,2], [3,4]]))
    print(my.countComponents(5, [[0,1], [1,2], [2,3], [3,4]]))

    print(my.countComponentsUnionFind(5, [[0,1], [1,2], [3,4]]))
    print(my.countComponentsUnionFind(5, [[0,1], [1,2], [2,3], [3,4]]))




