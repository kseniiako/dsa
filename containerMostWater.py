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
class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_volume = 0
        while left<right:
            print(left, right)
            cur_volume = min(height[left], height[right]) * (right - left)
            max_volume = max(cur_volume, max_volume)
            if height[left] <= height[right]:
                new_left = left

                while new_left < right:
                    if height[new_left] > height[left]:
                        break
                    new_left += 1
                
                left = new_left
            
            else:
                new_right = right

                while new_right > left:
                    if height[new_right] > height[right]:
                        break
                    new_right -= 1

                right = new_right

        return max_volume
                

if __name__ == "__main__":
    my = Solution()
    print(my.maxArea([1,8,6,2,5,4,8,3,7]))
    print(my.maxArea([1,1]))
    print(my.maxArea([1,2,1]))



        
        
        

