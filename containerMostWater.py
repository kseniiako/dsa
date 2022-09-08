# Container With Most Water (Leetcode 11)

# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0)
# and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that
# the container contains the most water.

# Return the max amount of water a container can store. Note that
# you cannot slant the container.

# The brute-force solution (checking all possible pairs of container "walls")
# would require O(n^2) time. How can we improve on that?

# There are two factors that positively contribute to the volume:
# distance between two container walls and height of the smaller container wall.
# To maximize volume, let's start at the greatest width (container is as wide as the 
# height array is long; indices 0 and len(height)-1 indicate the walls). Save this
# initial volume in max_volume.
# Now it would only make sense to reduce width if we come upon taller walls
# closer to the center of the array. So we choose the shorter (bottleneck) wall
# and move it inwards until we find a taller wall. We update max_volume
# to be the max of itself and new volume. Then we find the bottleneck wall again and
# proceed to move it inwards until we reach a taller alternative, etc. We stop when
# the condition left < right is not satisfied anymore: at this point, we can't reduce
# volume, and all relevant wall combinations have already been looked at.

# The intuition behind this algorithm is very greedy!

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_volume = 0

        # while a container is valid/has positive volume...
        while left<right:
            
            # find current volume and update max_volume
            cur_volume = min(height[left], height[right]) * (right - left)
            max_volume = max(cur_volume, max_volume)

            # now find the bottleneck/shorter wall. Step inwards
            # until a taller alternative to it is reached.
            # if the bottleneck is left, move the left wall rightwards.
            if height[left] <= height[right]:
                new_left = left

                while new_left < right:
                    if height[new_left] > height[left]:
                        break
                    new_left += 1
                
                left = new_left
            
            # if the bottleneck is right, move right wall leftwards.
            else:
                new_right = right

                while new_right > left:
                    if height[new_right] > height[right]:
                        break
                    new_right -= 1

                right = new_right

        return max_volume

        # Time complexity: we perform one pass over the array. O(n).
        # Space complexity: only a handful constant-space extra variables
        # are used. O(1).
                

if __name__ == "__main__":
    my = Solution()
    print(my.maxArea([1,8,6,2,5,4,8,3,7]))
    print(my.maxArea([1,1]))
    print(my.maxArea([1,2,1]))



        
        
        

