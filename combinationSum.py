# Combination Sum (Leetcode 39)

# import copy

class Solution:
    def combinationSum(self, candidates, target):
        # how to avoid redundant solutions?
        # backtracking + selecting the candidates in order.
        # Once we move on to add ith candidate to the combination,
        # we cannot add candidates from 0 to i-1 in the next explorations. 

        # This backtracking algo is unfolding as a DFS (depth-first search)
        # tree traversal.
        output = []
        # Populate the combinations, starting with current combination
        # comb. We have the remaining sum to fulfill (remain) and the current
        # cursor (start) to the list of candidates. 
        def backtrack(comb, remain, start):
            nonlocal output
            if remain == 0:
                # we append a deep copy of the current combination
                # so that it does not undergo changes as we backtrack!
                output.append(list(comb))
                return
    
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                cand = candidates[i]
                comb.append(cand)
                backtrack(comb, remain - cand, i)

                comb.pop()
            
        backtrack([], target, 0)
        
        return output

# Take note of when you deep copy, and when you push/pop (make
# changes in place and then potentially reverse them)!
# The idea is that you don't want to deep copy everything ->
# Potentially O(n^2) space! But you do want to deep copy everything
# that goes into the output so that the output does not change later
# as we backtrack!!!


if __name__ == "__main__":
    my = Solution()
    print(my.combinationSum([2,3,6,7], 7))
        



