# Last Stone Weight (Leetcode 1046)

# You are given an array of integers stones, where
# stones[i] is the weight of the ith stone. 

# We are playing a (cruel and dramatic) game with stones.
# On each turn, we choose the heaviest two stones and smash 
# them together. Suppose the heaviest two stones have weights
# x and y with x <= y. If x == y, both stones are destroyed
# in the smash. If x != y (that is, x < y), then the stone of
# weight x is destroyed and the stone of weight y has new weight
# y - x. 

# At the end of the game, there is at most one stone left.
# Return its weight. If there are no stones left, return 0.

import heapq

# The tricky aspect of this algorithm is that python
# only provides a minheap implementation in the heapq
# module, whereas here we need a maxheap. We can simply switch 
# the sign on all the stone weights (all weights are positive) to
# make the minheap suit our needs.

class Solution:
    def lastStoneWeight(self, stones):
        
        # create a minheap for stone weights with inverted sign
        # (functions as a maxheap for actual weights)
        stones_inverted = [-stone for stone in stones]
        heapq.heapify(stones_inverted)

        # pop largest (y) and second largest (x) stones 
        # from the heap
        while len(stones_inverted) > 1:
            y = heapq.heappop(stones_inverted)
            x = heapq.heappop(stones_inverted)
            
            # if stones have different weights, push the (inverted)
            # difference between them onto the heap
            if x > y:
                heapq.heappush(stones_inverted, (y-x))

        # return last remaining stone weight or zero
        if not stones_inverted:
            return 0
        else:
            return -stones_inverted[0]

if __name__ == "__main__":
    my = Solution()

    print(my.lastStoneWeight([2,7,4,1,8,1]))
    print(my.lastStoneWeight([1]))
