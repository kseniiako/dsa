# We're given an array of integers nums containing n+1 integers
# where each integer is in the range [1, n] inclusive. There
# is one repeated number. Return it. 

class Solution:
    def findDup(self, arr):
        length = len(arr)
        gauss = length * (length - 1) / 2
        sum_arr = 0
        for x in arr:
            sum_arr += x
        return sum_arr - gauss
    
    def findDupNew(self, arr):
        st = set()
        for x in arr:
            if x in st:
                return x
            else:
                st.add(x)

    def HashmapNegatives(self, arr):
        cur_ind = 0
        while arr[cur_ind] >= 0:
            tmp = arr[cur_ind]
            arr[cur_ind] *= -1
            cur_ind = tmp

        return cur_ind

    def HashmapRecursive(self, arr):

        cur = 0

        def RecursiveHelper(cur, arr):
            if arr[cur] < 0:
                return cur
            else:
                tmp = arr[cur]
                arr[cur] *= -1
                return RecursiveHelper(tmp, arr)
        
        return RecursiveHelper(cur, arr)
    
    def recursive2(self, arr):
        # this is recursion with using the array as
        # hashmap but without flipping signs
        # on numbers
        def recursive2helper(cur, arr):
            if cur == arr[cur]:
                return cur
            arr[cur], cur = cur, arr[cur]
            return recursive2helper(cur, arr)
        
        start_ind = 0
        return recursive2helper(start_ind, arr)

    
    def HashmapIterative(self, arr):
        # basically repeating the previous approach in iterative form
        # instead of recursive in order to save stack space!
        # (O(1) vs O(n))
        cur = 0
        while cur != arr[cur]:
            arr[cur], cur = cur, arr[cur]
        return cur

        # I like this solution — elegant!
        # Four lines if we use simultaneous assignment!

    def HashmapIterative0s(self, nums):
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]    

        # Three lines!

    def findDupl(self, nums):
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

    def binarySearch4Dup(self, nums):

        low = 0
        high = len(nums) - 1

        while low <= high:
            cur = (low + high) // 2
            count = 0

            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
        
        return duplicate

            



arr = []
my = Solution()
#print(my.findDup(arr))
#print(my.findDupNew(arr))

#import pdb; pdb.set_trace()
print(my.findDupl(arr))

