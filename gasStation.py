# Gas Station (Leetcode 134)

# There are n gas stations along a circular route, where the 
# amount of gas at the ith station is gas[i]. You have a car with
# an unlimited gas tank and it costs cost[i] of gas to travel from
# the ith station to the next. You begin the journey with an empty
# tank at one of the gas stations.
 
# Given two integer arrays gas and cost, return the starting station's
# index if you can travel along the circuit once in the clockwise
# direction, otherwise return -1. If a solution exists, it is guaranteed
# to be unique.

# As with most greedy problems, the biggest challenge here is identifying
# that the problem is greedy.

class Solution:
    def canCompleteCircuit(self, gas, cost):

        # check if there is enough gas to travel
        # over the whole array
        if sum(gas) < sum(cost):
            return -1

        cur_gas = 0
        start_station = 0
        i = 0

        # iterate over the whole array
        while i < len(gas):

                # find net gas balance for current stop
                net_gas = gas[i] - cost[i]
                
                # if you run out of gas on the way
                # to next stop, try starting at next stop
                if cur_gas + net_gas < 0:
                    # you start with 0 gas at the new start stop
                    cur_gas = 0
                    start_station = i+1
                # else update current gas balance to include net_gas 
                # from previous stop
                else:
                    cur_gas += net_gas

                i += 1
        
        return start_station
    
    # O(3n) -> O(n) time (one pass over the array + two sums 
    # over n-sized arrays). 
    # O(1) space: we only allocate space for a constant number of
    # additional values.

    # There is a very greedy intuition behind this algorithm.
    # First, we check if there is overall enough gas to sustain us.
    # If not, return false. If yes, proceed: now you know you will 
    # have enough gas to travel, it is just a matter of finding the
    # right start point.
    # You start traversing the array with 0 gas. If the first 
    # net_gas value (gas[i]-cost[i]) is negative, you can't start
    # traversing the array at index i. Therefore you should try
    # index i+1.
    # Say you are at point i+x when you determine start point i is
    # invalid (when you run out of gas on the way to i+x). The next
    # start point worth trying is i+x+1. All the points before that since
    # i have been reached with non-negative balance (otherwise start point
    # would have changed). Yet with that balance you still ran out of gas
    # at i+x. This means that you could not have started with 0 gas at any
    # of those points and not run out at i+x (or earlier).
    # We know that the answer is unique, and at start point
    # i all start points [0, i-1] have been pronounced invalid. Because
    # there is at least as much total gas as total costs (or more), we
    # know that since points [0, i-1] provide negative net_gas (put together),
    # points [i, len(gas)-1] must provide enough positive net_gas to carry
    # us through [0, i-1]. So unless starting with i provides negative 
    # net_gas on the slice [i, len(gas)-1] (which causes us to switch
    # examination to the next start point), we know we can loop over the 
    # whole array starting with i.

    # We can get rid of the time cost of summing over the cost and gas arrays
    # upfront by slightly tweaking the algorithm as below.

    def canCompleteCircuit1(self, gas, cost):
        # In this approach, we check whether the total
        # gas amount is valid (if sum(gas)>=sum(cost) or,
        # in other words, if sum of net costs over all stops
        # >= 0) simultaneously with searching for the start point
        # as we traverse the array. If total_gas < 0 by the end
        # of the loop, even if a certain start point is valid on a 
        # given slice, it cannot be valid over the whole array, (not
        # enough gas to offset all the costs!), and we return -1.
        cur_gas = total_gas = 0
        start_station = 0
        i = 0

        # iterate over the whole array
        while i < len(gas):

                # find net gas balance for current stop
                net_gas = gas[i] - cost[i]
                total_gas += net_gas
                
                # if you run out of gas on the way
                # to next stop, try starting at next stop
                if cur_gas + net_gas < 0:
                    # you start with 0 gas at the new start stop
                    cur_gas = 0
                    start_station = i+1
                # else update current gas balance to include net_gas 
                # from previous stop
                else:
                    cur_gas += net_gas

                i += 1
        
        return start_station if total_gas >= 0 else -1

        # O(n) time, constant (O(1)) space.

    def canCompleteCircuit2(self, gas, cost):
        # A bit convoluted but interesting solution from Neetcode. 
        # It traverses the list from both sides (two pointers travelling
        # towards each other) in the spirit of the "circular" nature of the 
        # complete trip (i. e. to determine if a start node is valid, we have 
        # to keep track of the total as the car traverses the right side of 
        # the array, and then the left side after "turning around the corner").

        start, end = len(gas) - 1, 0
        total = gas[start] - cost[start]

        # Here we move from two sides of the array at the same time,
        # keeping track of the total cost. (Start is the right side of
        # the array, end is the left side.)
        while start >= end:
            # Begin by moving start as fas left as possible
            # to traverse left from all the invalid nodes. The
            # first valid node is one where total (a value now summarizing
            # net costs over the whole right side of the array at and
            # after start) is nonnegative.
            while total < 0 and start >= end:
                start -= 1
                total += gas[start] - cost[start]
            # If start stopped before becoming smaller than end 
            # (start is at the same point as end), it means start == 
            # end == valid_node.
            if start == end:
                return start
            # If start has not reached the end (it stopped
            # traversing the list at the first valid node), traverse
            # from the left/end side and keep track of the
            # total.
            total += gas[end] - cost[end]
            end +=1
        
        # If we have not reached a point start == end, the total cost
        # is invalid. Traversal is not possible.
        return -1

        # For all the head-wrapping, asymptotically this solution 
        # has exactly the same performance as the previous one.

if __name__ == "__main__":
    my = Solution()
    print(my.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(my.canCompleteCircuit([2,3,4], [3,4,3]))
    print(my.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))

    print(my.canCompleteCircuit1([1,2,3,4,5], [3,4,5,1,2]))
    print(my.canCompleteCircuit1([2,3,4], [3,4,3]))
    print(my.canCompleteCircuit1([5,1,2,3,4], [4,4,1,5,1]))

    print(my.canCompleteCircuit2([1,2,3,4,5], [3,4,5,1,2]))
    print(my.canCompleteCircuit2([2,3,4], [3,4,3]))
    print(my.canCompleteCircuit2([5,1,2,3,4], [4,4,1,5,1]))
        
