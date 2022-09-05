# Combination Sum II (Leetcode 40)

# Given a collection of candidate numbers and a target number, find all
# unique combinations in candidates where the candidate numbers sum to
# target.
# Each number in candidates may only be used once in the combination.
# Note: the solution set bust not contain duplicat combinations.

class Solution:
    def combinationSum2(self, candidates, target):
        # Sort all the numbers in candidates
        cands_sorted = sorted(candidates)

        # Create an empty list for output and an empty list to keep
        # the current available combinations that we'll be working with
        output = []
        combs_set = []
        
        # recursively called backtracking function

        # In this function, we proceed to try and add every next element in the
        # input array to the combs_set until we come across an element of the same
        # value as its predecessor. Once the latter happens, we loop back to see how
        # many elements of this value we've encountered. Next, we only try adding this
        # element to combinations which already contain all the previously encountered
        # instances of this value. E. g. if it is the third 4, then we only add it to
        # elements of the combs_set which already have two 4s. This helps us avoid repeats
        # in the output, since if we add the third 4 to a set with one or zero 4s already present,
        # we'll get the same numbers of fours as were already explored and added to the collection
        # of possible combinations. 
        # Of course, the general rule applies whether an element is a repeat or not: added a new 
        # element? now backtrack! 
        # Note: combs_set and new_combs_set change places sinces we can't modify a collection right 
        # as we are going through its elements as a loop invariant.
        def backtrack(i, combs_set):
            new_combs_set = []

            cur = cands_sorted[i]
            if i == 0 or cur != cands_sorted[i-1]:
                if cur == target:
                    output.append([cur])

                else:
                    if cur < target:
                        new_combs_set.append([cur])
                    for elem in combs_set:
                        new_combs_set.append(list(elem))

                        sum_combination = cur
                        for x in elem:
                            sum_combination += x

                        if sum_combination <= target:
                            elem.append(cur)
                            if sum_combination < target:
                                new_combs_set.append(list(elem))
                            else:
                                output.append(elem)

            elif cur == cands_sorted[i-1]:
                num = 0
                i_start = i-1
                while i >= 0 and cands_sorted[i_start] == cur:
                    num += 1
                    i_start -= 1

                for elem in combs_set:
                    new_combs_set.append(list(elem))

                    if len(elem) >= num and elem[-num] == cur:
                        sum_combination = cur
                        for x in elem:
                            sum_combination += x

                        if sum_combination <= target:
                            elem.append(cur)
                            if sum_combination < target:
                                new_combs_set.append(list(elem))
                            else:
                                output.append(elem)
                
            combs_set = list(new_combs_set)

            if i < len(cands_sorted) - 1:
                backtrack(i+1, combs_set)
        
        backtrack(0, combs_set)
        return output

    def combinationSum2Elegant(self, candidates, target):
        # While my initial solution works, here is the one form Neetcode
        # which I believe is more elegant and succinct.

        cands_sorted = sorted(candidates)
        output = []

        def backtrack(current_comb, position, target):
            if target == 0:
                output.append(list(current_comb))
            # Nice design choice: if a combination has reached 
            # target, we need to return no matter if it is valid or not. 
            if target <= 0:
                return
            
            prev = -1
            for i in range(position, len(cands_sorted)):
                if cands_sorted[i] == prev:
                    continue
                cur.append(cands_sorted[i])
                backtrack(current_comb, i + 1, target - cands_sorted[i])
                cur.pop()

                prev = cands_sorted[i]
            
        backtracks([], 0, target)
        return output

        # Here's what happens in this program. Say we have an array of seven 1s, and
        # we need to reach target 5. Every time we call backtrack, we examine
        # all the values at and after current index. We add the first value 
        # (at current index) w/o checking and send it to its own call to backtrack.
        # This absence of checking for just the first encountered value is facilitated
        # by setting prev (variable holding previously encountered value) to -1
        # in each new call to backtrack (-1 is an invalid value, we can never see it
        # in the input array). Then we reset the prev variable to previously
        # encountered value at each iteration and ignore all value repeats, only
        # calling backtrack for non-repeat values. What this means is that an n-long streak
        # of the same value in the sorted input array would result in just one sequence of calls
        # to backtrack, not in a tree of calls. Therefore, only one combination option
        # for each possible number of occurences of the repeat value (from 0 to n) would
        # be tested. Input of [1]*7 and target 5 would obly produce one combination
        # in output.

        # In this approach, we don't have to loop back in the input array to count previous occurences 
        # of value k at every index. We also don't have to check the number of ks already present in each 
        # element in combs_set to see whether adding a new k to this element is valid. Thus,
        # the second approach is significantly faster than the first one! (At least by the factor of n^3!)




        
if __name__ == "__main__":
    my = Solution()
    #print(my.combinationSum2([2,3,6,7], 7))
    #print(my.combinationSum2([2,3,5], 8))
    print(my.combinationSum2([10,1,2,7,6,1,5], 8))
    print(my.combinationSum2([2,5,2,1,2], 5))


                

                