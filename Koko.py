# Koko eating bananas! (LC 875)

# Koko loves to eat bananas. There are n piles of bananas,
# the ith pile has piles[i] bananas. The guards have gone and
# will come back in h hours. 

# Koko can decide her bananas-per-hour eating speed of k. 
# Each hour, she chooses some pile of bananas and eats k 
# bananas from that pile. If the pile has less than k bananas,
# she eats all of them instead and will not eat any more
# bananas during this hour. 

# Koko likes to eat slowly but still wants to finish eating all
# the bananas before the quards return. 
 
# return the minimum int k s. t. she can eat all the bananas
# within h hours. 

from math import ceil

class Solution():
    def minEatingSpeed(self, piles, h):
        # my first take at binary search for this
        # problem.
        
        max_speed = 0
        total_bananas = 0
        for x in piles:
            if x > max_speed:
                max_speed = x
            total_bananas += x
        
        min_speed = ceil(total_bananas/h)

        output = -1 

        while min_speed <= max_speed:

            mid_speed = (min_speed + max_speed) // 2

            time_spent = 0
            for x in piles:
                time_spent += ceil(x/mid_speed)
            
            if time_spent <= h:
                output = mid_speed
                max_speed = mid_speed - 1

            else:
                min_speed = mid_speed + 1

        return output
    
    def minEatingSpeed2(self, piles, h):
        # same solution, different style of
        # setting up search algorithm
        
        max_speed = 0
        total_bananas = 0
        for x in piles:
            if x > max_speed:
                max_speed = x
            total_bananas += x
        
        min_speed = ceil(total_bananas/h)

        while min_speed < max_speed:

            mid_speed = (min_speed + max_speed) // 2

            time_spent = 0
            for x in piles:
                time_spent += ceil(x/mid_speed)
            
            if time_spent <= h:
                max_speed = mid_speed

            else:
                min_speed = mid_speed + 1

        return min_speed

piles1 = [3,6,7,11]
h1 = 8  

piles2 = [30,11,23,4,20]
h2 = 5

piles3 = [30,11,23,4,20]
h3 = 6

my = Solution()
print(my.minEatingSpeed(piles1, h1))
print(my.minEatingSpeed(piles2, h2))
print(my.minEatingSpeed(piles3, h3))

print(my.minEatingSpeed2(piles1, h1))
print(my.minEatingSpeed2(piles2, h2))
print(my.minEatingSpeed2(piles3, h3))