# here I'm going to solve find duplicate number (LC 287)
# with a binary search-based approach.

# this problem is a great candidate for binary search
# because we can sort the numbers so that
# they appear in nondecreasing order!

class Solution:
    def insSort(self, lst):

        if len(lst) < 2:
            return lst

        out = []

        out.append(lst[0])
        for i in range(1, len(lst)):
            out.append(lst[i])
            for x in range(len(out)-1, 0, -1):
                if out[x] < out[x-1]:
                    out[x], out[x-1] = out[x-1], out[x]
        return out

    def findDupSearch(self, lst):

        lst_sorted = self.insSort(lst)
        start = 0
        finish = len(lst_sorted) - 1 

        # default option: duplicate not found
        out = -1 

        while start <= finish:

            mid = (start + finish) // 2
            if mid >= lst_sorted[mid]:
                out = lst_sorted[mid]
                finish = mid - 1
            else:
                start = mid + 1
        return out
    
    def findDupSearch2(self, lst):
        # in this implementation, we do not pre-sort the
        # list. Instead, we binary sort the list, examining the mid at
        # each step. This runs in O(nlogn). So same asymptotic time as
        # the previous algorithm. 
        start = 1
        finish = len(lst) - 1

        out = -1

        while start <= finish:
            mid = (start + finish) // 2

            count = 0
            for x in lst:
                if x <= mid:
                    count += 1
            
            if count > mid:
                out = mid
                finish = mid - 1
            else:
                start = mid + 1

        return out


my = Solution()
lst = [1, 2, 3, 3]
#import pdb; pdb.set_trace()
print(my.findDupSearch2(lst))